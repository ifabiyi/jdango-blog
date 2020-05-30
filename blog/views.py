from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

posts = [
    {
        'author': ' Mayowa',
        'title': 'First blog post',
        'content': 'Awww and  here comes the first',
        'date': 'June 23 2020' 
    },

    {
        'author': ' Ifabiyi',
        'title': 'Second blog post',
        'content': 'Awww and  here comes the second',
        'date': 'June 24 2020' 
    }
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
