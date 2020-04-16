from django.shortcuts import render

def testim(request):
    return render(request, 'testing.html', {'title': 'About'})

def about(request):
    return render(request, 'about.html', {'title': 'About'})