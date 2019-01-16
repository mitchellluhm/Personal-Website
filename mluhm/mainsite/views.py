from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from django.template import loader
from django.views.generic import (TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView)

from mainsite.models import Post
from mainsite.forms import PostForm

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.utils import timezone

# Create your views here.
def index(request):
    latest_posts = Post.objects.filter(publish_date__lte=timezone.now()).order_by('-publish_date')
    most_rec = latest_posts[0]
    most_rec2 = latest_posts[1]
    
    template = loader.get_template('post_list.html')
    context = {
        'latest_posts' : latest_posts,
        'most_rec' : most_rec,
        'most_rec2' : most_rec2,
    }

    return HttpResponse(template.render(context, request))

def blog(request):
    latest_posts = Post.objects.filter(publish_date__lte=timezone.now()).order_by('-publish_date')
    template = loader.get_template('blog.html')

    context = {
        'latest_posts' : latest_posts,
    }
    return HttpResponse(template.render(context, request))

def projects(request):
    template = loader.get_template('projects.html')
    return HttpResponse(template.render({}, request))

def about(request):
    template = loader.get_template('about.html')
    return HttpResponse(template.render({}, request))

def contact(request):
    template = loader.get_template('contact.html')
    return HttpResponse(template.render({}, request))

def post_detail(request, pk):
    # find blog post with specified parameter
    try:
        post = Post.objects.get(pk=pk)
    except:
        raise Http404("This post does not exist.")

    template = loader.get_template('post_detail.html')
    context = {'post' : post}

    return HttpResponse(template.render(context, request))

@login_required
def post_new(request):
    template = loader.get_template('post_form.html')
    form = PostForm
    context = {
        'form' : form
    }

    return HttpResponse(template.render(context, request))
    

class AboutView(TemplateView):
    template_name = 'about.html'

class PostListView(ListView):
    model = Post

    # adding
    template_name = 'post_list.html'

    def get_queryset(self):
        # "FIELD LOOKUPS"
        return Post.objects.filter(publish_date__lte=timezone.now()).order_by('-publish_date')

class PostDetailView(DetailView):
    model = Post

    # get individual page

class CreatePostView(LoginRequiredMixin, CreateView):
    # don't want everyone to access this create post view
    login_url = '/login/'
    redirect_field_name = 'post_detail.html'
    form_class = PostForm
    model = Post

class PostUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/login/'
    redirect_field_name = 'post_detail.html'
    form_class = PostForm
    model = Post

class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('post_list')

class DraftListView(LoginRequiredMixin, ListView):
    login_url = '/login/'
    redirect_field_name = 'post_list.html'
    model = Post

    def get_queryset(self):
        return Post.objects.filter(publish_date__isnull=True).order_by('created_date')

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

@login_required
def post_publish(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.publish
    return redirect('post_detail', pk=pk)
