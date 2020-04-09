from django.shortcuts import render

# Dummy data
dummy_notices = [
    {
        'author': 'CoreyMS',
        'title': 'Blog Post 1',
        'body': 'First post content',
        'created_at': 'August 27, 2018'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'body': 'Second post content',
        'created_at': 'July 30, 2018'
    },
    {
        'author': 'Ronny Nose',
        'title': 'Blog Post 3',
        'body': 'New something something',
        'created_at': 'April 3, 2019'
    }
]

def home(request):
    context = {
        'notices': dummy_notices
    }
    return render(request, 'vv_app/home.html', context)

def about(request):
    return render(request, 'vv_app/about.html', {'title': 'About'})