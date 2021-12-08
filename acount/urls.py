from django.urls import path
from .views import ArticleListView, ArticleCreateView, ArticleUpdateView, DeleteArticleView, ProfileView

app_name = 'accounts'

urlpatterns = [
    path('', ArticleListView.as_view(), name='home'),
    path ('article/create/', ArticleCreateView.as_view(), name='article_create'),
    path ('article/update/<int:pk>/', ArticleUpdateView.as_view(), name='article_update'),
    path ('article/delete/<int:pk>/', DeleteArticleView.as_view(), name='article_delete'),
    path ('profile/', ProfileView.as_view(), name='profile'),
]
