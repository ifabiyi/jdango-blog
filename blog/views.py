from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from django.views.generic import ListView, DetailView, CreateView, UpdateView
#for class based view
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)

#class based view without sticking to the convention
class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'   #<app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    #change the order of the post tothe latest
    ordering = ['-date_posted']

#blog detailed view  based on convention
class PostDetailView(DetailView):
    model = Post
    
    
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title','content']
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    fields = ['title','content']
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
