from django.urls import path
from .views import home, blog_single, blog_category

app_name = 'blog'
urlpatterns = [
    path('', home, name = 'home'),
    path('article/<slug:slug>/', blog_single, name = 'single'),
    path('category/<slug:slug>/', blog_category, name = 'category'),
]