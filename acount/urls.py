from django.contrib.auth import views
from django.urls import path
from .views import ArticleListView, ArticleCreateView, ArticleUpdateView, DeleteArticleView, ProfileView, PasswordChange

app_name = 'accounts'
urlpatterns = [
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),

    path('password_change/', PasswordChange.as_view(), name='password_change'),

    #path('password_reset/', views.PasswordResetView.as_view(), name='password_reset'),
    #path('password_reset/done/', views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    #path('reset/<uidb64>/<token>/', views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    #path('reset/done/', views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]

urlpatterns += [
    path('', ArticleListView.as_view(), name='home'),
    path ('article/create/', ArticleCreateView.as_view(), name='article_create'),
    path ('article/update/<int:pk>/', ArticleUpdateView.as_view(), name='article_update'),
    path ('article/delete/<int:pk>/', DeleteArticleView.as_view(), name='article_delete'),
    path ('profile/', ProfileView.as_view(), name='profile'),
]
