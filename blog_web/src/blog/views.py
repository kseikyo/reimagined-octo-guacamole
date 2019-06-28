from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
from django.utils import timezone

from .models import BlogPost
from .forms import BlogPostModelForm

# GET -> 1 object
# filter -> [] of objects


def blog_post_list_view(request):
	qs = BlogPost.objects.all().published()
	if request.user.is_authenticated:
		my_qs = BlogPost.objects.filter(user=request.user)
		qs    = (qs | my_qs).distinct()
	template_name = 'blog/list.html'
	context = {'object_list': qs}
	return render(request, template_name, context)

@staff_member_required
def blog_post_create_view(request):
	form = BlogPostModelForm(request.POST or None, request.FILES or None, initial={'publish_date': timezone.now()})
	if form.is_valid():
		obj = form.save(commit=False)
		obj.user = request.user
		obj.save()
		return redirect('/blog')
	template_name = 'form.html'
	context = {'form': form}
	return render(request, template_name, context)


def blog_post_read_view(request, post_slug):
	obj = get_object_or_404(BlogPost, slug=post_slug)
	template_name= 'blog/detail.html'
	context = {"object": obj}
	return render(request, template_name, context)

@staff_member_required
def blog_post_update_view(request, post_slug):
	obj = get_object_or_404(BlogPost, slug=post_slug)
	form = BlogPostModelForm(request.POST or None, instance=obj)
	if form.is_valid():
		form.save()
	template_name= 'form.html'
	context = {'form': form, "title": f"Update {obj.title}"}
	return render(request, template_name, context)

@staff_member_required
def blog_post_delete_view(request, post_slug):
	obj = get_object_or_404(BlogPost, slug=post_slug)
	template_name= 'blog/delete.html'
	if request.method == 'POST' and obj is not None:
		obj.delete()
		return redirect('/blog')
	context = {"object": obj}
	return render(request, template_name, context)