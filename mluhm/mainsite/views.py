from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
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
    template = loader.get_template('post_list.html')
    context = {
        'latest_posts' : latest_posts
    }

    return HttpResponse(template.render(context, request))

def about(request):
    template = loader.get_template('about.html')

    return HttpResponse(template.render({}, request))

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
