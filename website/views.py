from django.shortcuts import render

def web_home(request):
    return render(request, 'website/index.html')
