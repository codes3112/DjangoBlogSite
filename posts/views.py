from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import (ListView,
                                  DetailView,
                                  CreateView,
                                  UpdateView,
                                  DeleteView)
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from .models import Posts

# Create your views here.

def index(request):
    #return HttpResponse("Hello, world. You're at the posts index.")

    #create a variable posts to get the data
    posts=Posts.objects.all()
    # [:10]

    # create data object called context(variable)
    context={
        'title':'Latest Posts',
        'posts': posts        
    }

    # return render(request,'posts/index.html',{
    # 'title':'Latest Posts'
    # })
    return render(request,'posts/index.html',context)

class PostListView(ListView):
    model=Posts
    #<app>/<model>_<viewtype>.html
    template_name = 'posts/index.html'
    context_object_name = 'posts'
    ordering =  ['-created_at']

def details(request,id):
        try:
            post= Posts.objects.get(id=id)
        except Posts.DoesNotExist:
            raise Http404("Post does not exist")
        context={
        'post':post
                }
        return render(request,'posts/details.html',context)

class PostDetailView(DetailView):
    model=Posts
    #<app>/<model>_<viewtype>.html
    template_name = 'posts/details.html'
    context_object_name = 'post'

class PostCreateView(LoginRequiredMixin,CreateView):
    model=Posts
    fields = ['title','body']
    template_name = 'posts/post_form.html'
    #<app>/<model>_<viewtype>.html
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model=Posts
    fields = ['title','body']
    template_name = 'posts/post_form.html'
    #<app>/<model>_<viewtype>.html
    context_object_name = 'post'

    def test_func(self):
        post=self.get_object()
        if self.request.user == post.author:
            return True
        return False
        
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model=Posts
    #<app>/<model>_<viewtype>.html
    template_name = 'posts/post_confirm_delete.html'
    context_object_name = 'post'
    success_url='/'

    def test_func(self):
        post=self.get_object()
        if self.request.user == post.author:
            return True
        return False

    

    
       
