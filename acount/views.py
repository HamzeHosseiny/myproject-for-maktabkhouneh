from django.shortcuts import reverse
from django.urls import reverse_lazy
from .models import User
from .forms import ProfileForm
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .mixins import FieldMixin, FormValidationMixin, AuthorEditAccessMixin, AuthorsEditAccessMixin
from blog.models import Article
from django.http import HttpResponse
from django.shortcuts import render
from .forms import SignupForm
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.core.mail import EmailMessage

# Create your views here.

class ArticleListView(AuthorsEditAccessMixin, ListView):
    model = Article
    template_name = 'registration/home.html'
    #login_url = 'login'
    context_object_name = 'articles'
    def get_queryset(self):
        if self.request.user.is_superuser:
            return Article.objects.all()
        else:
            return Article.objects.filter(Author=self.request.user)


class ArticleCreateView(AuthorsEditAccessMixin, FieldMixin, FormValidationMixin, CreateView):
    model = Article
    template_name = 'registration/article_create.html'
    def get_success_url(self):
        return reverse('accounts:home')


class ArticleUpdateView(AuthorsEditAccessMixin,AuthorEditAccessMixin, FieldMixin, FormValidationMixin, UpdateView):
    model = Article
    template_name = 'registration/article_create.html'
    def get_success_url(self):
        return reverse('accounts:home')

class DeleteArticleView(AuthorsEditAccessMixin, AuthorEditAccessMixin, DeleteView):
    model = Article
    template_name = 'registration/article_delete.html'
    success_url = reverse_lazy('accounts:home')

class ProfileView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = ProfileForm
    template_name = 'registration/profile.html'

    def get_success_url(self):
        return reverse('accounts:profile')

    def get_object(self):
        return self.request.user
    
    def get_form_kwargs(self):
        kwargs = super(ProfileView, self).get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs


class Login(LoginView):

    def get_success_url(self):
        user = self.request.user

        if user.is_superuser or user.is_author:
            return reverse('accounts:home')
        else:
            return reverse('accounts:profile')


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            mail_subject = 'Activate your blog account.'
            message = render_to_string('registration/activation_account.html', {
                'user': user,
                'domain': current_site.domain,
                'uid':urlsafe_base64_encode(force_bytes(user.pk)),
                'token':account_activation_token.make_token(user),
            })
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(
                        mail_subject, message, to=[to_email]
            )
            email.send()
            return HttpResponse('Please confirm your email address to complete the registration')
    else:
        form = SignupForm()
    return render(request, 'registration/signup.html', {'form': form})


def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
    else:
        return HttpResponse('Activation link is invalid!')
