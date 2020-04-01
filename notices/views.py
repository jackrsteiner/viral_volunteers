from django.shortcuts import render

def home(request):
    return render(request, 'notices/home.html')

def about(request):
    return render(request, 'notices/about.html')