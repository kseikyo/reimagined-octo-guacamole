from django.conf import settings
from django.db import models
from django.db.models import Q
from django.utils import timezone
# Create your models here.

User = settings.AUTH_USER_MODEL
''' from django.contrib.auth import get_user_model
	User = get_user_model()
	User.objects.first().blogpost_set.all()
This shows all the blog posts from the first user
this method is used whenever you're not doing a login
'''
class BlogPostQuerySet(models.QuerySet):
	def published(self):
		time_now = timezone.now()
		return self.filter(publish_date__lte=time_now)

	def search(self, query):
		my_query = (Q(title__icontains=query) | Q(content__icontains=query))
		return self.filter(my_query) 

# A Manager is the interface through which database query operations are provided to Django models.
class BlogPostManager(models.Manager):
	def get_queryset(self):
		return BlogPostQuerySet(self.model, using=self._db)

	def published(self):
		return self.get_queryset().published()

	def search(self, query=None):
		if query is None:
			return self.get_queryset.none()
		return self.get_queryset().published().search(query)

class BlogPost(models.Model):
	
	user         = models.ForeignKey(User, default=1, on_delete=models.SET_NULL, null=True)
	image        = models.ImageField(upload_to='image/', blank=True, null=True)
	title  	     = models.CharField(max_length=120)
	content      = models.TextField(null=True, blank=True)
	slug	     = models.SlugField(unique=True)
	publish_date = models.DateTimeField(auto_now=False, auto_now_add=False, null=True, blank=True)
	timestamp    = models.DateTimeField(auto_now_add=True)
	updated      = models.DateTimeField(auto_now=True)
	objects      = BlogPostManager()

	class Meta:
		ordering = ['-publish_date', '-updated', '-timestamp']

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return f'/blog/{self.slug}'
	
	def get_edit_url(self):
		return f"{self.get_absolute_url()}/edit"
	
	def get_delete_url(self):
		return f"{self.get_absolute_url()}/delete"
	