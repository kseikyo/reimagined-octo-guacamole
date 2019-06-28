from django.urls import path, re_path   
from .views import (
    blog_post_create_view,
    blog_post_delete_view,
    blog_post_list_view,
    blog_post_read_view,
    blog_post_update_view,
)


urlpatterns = [
    path('<str:post_slug>/', blog_post_read_view, name='blog_post'),
    path('<str:post_slug>/edit', blog_post_update_view, name='blog_post_update'), 
    path('<str:post_slug>/delete', blog_post_delete_view, name='blog_post_delete'), 
    path('', blog_post_list_view),
    #re_path(r'^blog/(?P<post_id>\d+)/$', blog_post_detail_page, name='blog_post'), using regex to get only numbers as id
]
