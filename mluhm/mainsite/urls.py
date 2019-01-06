from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    re_path(r'^post/(?P<pk>\d+)$', views.post_detail, name='post_detail'),
    path('post/new/', views.CreatePostView.as_view(), name='post_new'),
    re_path(r'^post/(?P<pk>\d+)/edit/$', views.PostUpdateView.as_view(), name='post_edit'),
    re_path(r'^post/(?P<pk>\d+)/remove/$', views.PostDeleteView.as_view(), name='post_remove'),
    path('drafts/', views.DraftListView.as_view(), name='post_draft_list'),
    re_path(r'^post/(?P<pk>\d+)/publish/$', views.post_publish, name='post_publish'),
]
# path('', views.index, name='index'),
'''
path('', views.PostListView.as_view(), name='post_list'),
path('about/', views.AboutView.as_view(), name='about'),
re_path(r'^post/(?P<pk>\d+)$', views.PostDetailView.as_view(), name='post_detail'),
path('post/new/', views.CreatePostView.as_view(), name='post_new'),
re_path(r'^post/(?P<pk>\d+)/edit/$', views.PostUpdateView.as_view(), name='post_edit'),
re_path(r'^post/(?P<pk>\d+)/remove/$', views.PostDeleteView.as_view(), name='post_remove'),
path('drafts/', views.DraftListView.as_view(), name='post_draft_list'),
re_path(r'^post/(?P<pk>\d+)/publish/$', views.post_publish, name='post_publish'),
'''
