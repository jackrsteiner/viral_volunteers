from django.shortcuts import render
from notices.models import Notice

def home(request):
    context = {
        'notices': Notice.objects.all()
    }
    return render(request, 'vv_app/home.html', context)

def about(request):
    return render(request, 'vv_app/about.html', {'title': 'About'})