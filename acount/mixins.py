from django.http import Http404
from django.shortcuts import get_object_or_404, redirect
from blog.models import Article


class FieldMixin():

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_superuser:
            self.fields = ['title', 'Author', 'category', 'thumbnail', 'description', 'published_date', 'is_special', 'status']
        elif request.user.is_author:
            self.fields = ['title', 'category', 'thumbnail', 'description', 'is_special', 'published_date', 'status']
        else:
            raise Http404
        return super().dispatch(request, *args, **kwargs)


class FormValidationMixin():

    def form_valid(self, form):
        if self.request.user.is_superuser:
            form.save()
        elif self.request.user.is_author:
            form.instance = form.save(commit=False)
            form.instance.Author = self.request.user
            form.instance.status = "d"
            form.save()
        return super().form_valid(form)


class AuthorEditAccessMixin():

    def dispatch(self, request, pk, *args, **kwargs):
        article = get_object_or_404(Article, pk=pk)
        if article.Author == request.user and article.status in ['d', 'r'] or request.user.is_superuser:
            return super().dispatch(request, *args, **kwargs)
        else:
            raise Http404


class AuthorsEditAccessMixin():

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            if request.user.is_superuser or request.user.is_author:
                return super().dispatch(request, *args, **kwargs)
            else:
                return redirect('accounts:profile')
        else:
            return redirect('login')
