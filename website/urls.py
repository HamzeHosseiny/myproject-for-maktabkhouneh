from django.urls import path
from .views import web_home, ContactsView, AboutView, Newsletter

app_name = 'website'
urlpatterns = [
    path('', web_home, name = 'web_home'),
    path('contact/', ContactsView.as_view(), name = 'contact'),
    path('about/', AboutView, name = 'about'),
    path('Newsletter/', Newsletter, name = "Newsletter" ),
]