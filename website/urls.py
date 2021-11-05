from django.urls import path
from .views import web_home

app_name = 'website'
urlpatterns = [
    path('', web_home, name = 'web_home')
]