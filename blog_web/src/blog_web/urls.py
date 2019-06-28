"""URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.urls import path, re_path, include  
from searches.views import search_view

from blog.views import (
    blog_post_create_view
)
from .views import (
    about_page,
    contact_page, 
    home_page,
)

urlpatterns = [
    path('about/', about_page, name="about"),
    path('admin/', admin.site.urls),
    path('blog-new', blog_post_create_view),
    path('blog/', include('blog.urls')),
    #re_path(r'^blog/(?P<post_id>\d+)/$', blog_post_detail_page, name='blog_post'), using regex to get only numbers as id
    path('contact/', contact_page, name="contact"),
    path('search/', search_view, name='search'),
    path('', home_page, name="home"),
]

#ONLY USING THIS TO SEE THE IMAGE ADDED TO THE BLOG_POST ON ADMIN PAGE IN A URL
if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)