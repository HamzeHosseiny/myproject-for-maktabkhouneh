from django.urls import path
from .views import ArticleListView, ArticleDetailView, ArticleCategoryView, AuthorArticleListView, ArticlePreviewView, SearchListView

app_name = 'blog'
urlpatterns = [
    path('', ArticleListView.as_view(), name = 'home'),
    path('article/<slug:slug>/', ArticleDetailView.as_view(), name = 'single'),
    path('category/<slug:slug>/', ArticleCategoryView.as_view(), name = 'category'),
    path('Author/<slug:username>/', AuthorArticleListView.as_view(), name = 'author'),
    path('search/', SearchListView.as_view(), name = 'search'),
    path('search/page/<int:page>', SearchListView.as_view(), name = 'search'),
    path('preview/<int:pk>/', ArticlePreviewView.as_view(), name = 'preview'),
]