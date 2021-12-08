from django.shortcuts import render
from django.shortcuts import reverse
from .models import Contacts
from django.views.generic import CreateView, DetailView


def web_home(request):
    return render(request, 'website/index.html')


class ContactsView(CreateView):
    model = Contacts
    fields = ['name', 'email', 'message']
    template_name = 'website/contact.html'
    def get_success_url(self):
        return reverse('website:web_home')

def AboutView(request):
    return render(request, 'website/about.html')