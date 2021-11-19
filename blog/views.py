from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.core.paginator import Paginator
from .models import Article, Category
from django.contrib.auth.models import User

#def home(request):
#    articles = Article.objects.published()
#    paginator = Paginator(articles, 1)
#    page = request.GET.get('page')
#    articles = paginator.get_page(page)
#    context = {'Articles': articles}
#    return render(request, 'blog/blog.html', context)
 
class ArticleListView(ListView):
    model = Article
    template_name = 'blog/blog.html'
    context_object_name = 'Articles'
    paginate_by = 6

    def get_queryset(self):
        return Article.objects.published()

#def blog_single(request, slug):
#    article = get_object_or_404(Article.objects.published(), slug = slug)
#    context = {'Article': article}
#    return render(request, 'blog/blog-single.html', context)

class ArticleDetailView(DetailView):
    model = Article
    template_name = 'blog/blog-single.html'
    context_object_name = 'Article'

    def get_object(self):
        slug = self.kwargs.get('slug')
        return get_object_or_404(Article.objects.published(), slug = slug)

#def blog_category(request, slug):
#    category = get_object_or_404(Category, slug = slug)
#    articles = Article.objects.filter(category = category, status= 'p')
#    paginator = Paginator(articles, 1)
#    page = request.GET.get('page')
#    articles = paginator.get_page(page)
#    context = {'Category': category, 'Articles': articles}
#    return render(request, 'blog/blog-category.html', context)

class ArticleCategoryView(ListView):
    model = Article
    template_name = 'blog/blog-category.html'
    context_object_name = 'Articles'
    paginate_by = 1

    def get_queryset(self):
        global category
        slug = self.kwargs.get('slug')
        category = get_object_or_404(Category, slug = slug)
        return Article.objects.filter(category = category, status= 'p')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Category'] = category
        return context

class AuthorArticleListView(ListView):
    model = Article
    template_name = 'blog/blog-author.html'
    context_object_name = 'Articles'
    paginate_by = 1
    def get_queryset(self):
        global author
        author = get_object_or_404(User, username = self.kwargs.get('username'))
        return Article.objects.filter(Author = author, status= 'p')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Author'] = author
        return context