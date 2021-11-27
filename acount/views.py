from django.shortcuts import reverse
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from .models import User
from .forms import ProfileForm
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .mixins import FieldMixin, FormValidationMixin, AuthorEditAccessMixin, AuthorsEditAccessMixin
from blog.models import Article

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

class ProfileView(UpdateView):
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

class PasswordChange(PasswordChangeView):
    template_name = 'registration/password_change.html'
    success_url = reverse_lazy('accounts:profile')