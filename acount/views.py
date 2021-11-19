from django.shortcuts import render
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from blog.models import Article

# Create your views here.

class ArticleListView(LoginRequiredMixin, ListView):
    model = Article
    template_name = 'registration/home.html'
    #login_url = 'login'
    query_set = Article.objects.all()
