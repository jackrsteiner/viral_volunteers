from django.shortcuts import render

# Dummy data
posts = [
    {
        'author': 'CoreyMS',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'August 27, 2018'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'July 30, 2018'
    }
]

def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'vv_app/home.html', context)

def about(request):
    return render(request, 'vv_app/about.html', {'title': 'About'})