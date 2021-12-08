from acount.models import User
from .models import Article, Category
from django.shortcuts import get_object_or_404
from acount.mixins import AuthorEditAccessMixin
from django.views.generic import ListView, DetailView

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
    paginate_by = 1

    def get_queryset(self):
        return Article.objects.published()

class SearchListView(ListView):
    model = Article
    template_name = 'blog/search.html'
    context_object_name = 'Articles'
    paginate_by = 1

    def get_queryset(self):
        search = self.request.GET.get('q')
        if not search:
            return Article.objects.none()
        else:
            return Article.objects.filter(description__icontains=search)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search'] = self.request.GET.get('q')
        return context
  
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
        article = get_object_or_404(Article.objects.published(), slug = slug)
        
        ip_address = self.request.user.ip_address
        if ip_address not in article.hits.all():
            article.hits.add(ip_address)
            article.save()

        return article


class ArticlePreviewView(AuthorEditAccessMixin, DetailView):
    model = Article
    template_name = 'blog/blog-single.html'
    context_object_name = 'Article'

    def get_object(self):
        pk = self.kwargs.get('pk')
        return get_object_or_404(Article, pk = pk)


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
