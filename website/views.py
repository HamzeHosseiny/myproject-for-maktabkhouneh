from django.shortcuts import render, HttpResponseRedirect
from .models import Contacts
from django.views.generic import CreateView
from .forms import NewsletterForm


def web_home(request):
    return render(request, 'website/index.html')


class ContactsView(CreateView):
    model = Contacts
    fields = ['name', 'email', 'message']
    template_name = 'website/contact.html'


def AboutView(request):
    return render(request, 'website/about.html')


def Newsletter(request):
	if request.method == 'POST':
		news = NewsletterForm(request.POST)
		if news.is_valid():
			news.save()
			return HttpResponseRedirect('/')
		else:
			return HttpResponseRedirect('/')
