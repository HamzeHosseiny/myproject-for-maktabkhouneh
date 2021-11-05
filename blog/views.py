from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Article, Category

def home(request):
    articles = Article.objects.published()
    paginator = Paginator(articles, 1)
    page = request.GET.get('page')
    articles = paginator.get_page(page)
    context = {'Articles': articles}
    return render(request, 'blog/blog.html', context)

def blog_single(request, slug):
    article = get_object_or_404(Article.objects.published(), slug = slug)
    context = {'Article': article}
    return render(request, 'blog/blog-single.html', context)

def blog_category(request, slug):
    category = get_object_or_404(Category, slug = slug)
    articles = Article.objects.filter(category = category, status= 'p')
    paginator = Paginator(articles, 1)
    page = request.GET.get('page')
    articles = paginator.get_page(page)
    context = {'Category': category, 'Articles': articles}
    return render(request, 'blog/blog-category.html', context)
