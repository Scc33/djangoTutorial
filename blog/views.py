from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'author': 'Sean C',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'June 27, 2020'
    },
    {
        'author': 'Sean C',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'June 27, 2020'
    }
]

def home(request):
    context = {
        'title': 'Home',
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
