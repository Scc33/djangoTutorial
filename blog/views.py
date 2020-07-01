from django.shortcuts import render
from django.views.generic import ListView
# from django.http import HttpResponse
from .models import Post

'''
Class based views
'''

class PostListView(ListView):
    model = Post
    # expected template name -> <app>/<model>_<viewtype>.html
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted'] # reverses the ordering so newest posts first

'''
Function based views
'''

def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
