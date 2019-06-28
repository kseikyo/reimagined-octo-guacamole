from django.shortcuts import render
from .forms import ContactForm
from blog.models import BlogPost


def home_page(request):
	my_title = "Welcome to my blog!"
	qs = BlogPost.objects.all().published()[:5]
	context  = {"title": my_title, "blog_list": qs}
	return render(request, "home.html", context)


def contact_page(request):
	my_title = "Contact us"
	form = ContactForm(request.POST or None)
	if form.is_valid():
		pass
	context = {
	"title": my_title,
	"form": form
	}
	return render(request, "form.html", context)


def about_page(request):
	my_title = "About us"
	my_text  = "This is about us"
	return render(request, "about.html", {"title": my_title, "text": my_text})

