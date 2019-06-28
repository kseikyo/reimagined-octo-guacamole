from django import forms
from .models import BlogPost
from django.utils import timezone

class BlogPostForm(forms.Form):
    title   = forms.CharField()
    slug    = forms.SlugField()
    content = forms.CharField(widget=forms.Textarea)

class BlogPostModelForm(forms.ModelForm):
    class Meta:
        model  = BlogPost                             #YEAR-MONTH-DATE
        fields = ['title', 'image', 'slug', 'content', 'publish_date']

    def clean_title(self, *args, **kwargs):
        instance = self.instance
        title = self.cleaned_data.get('title')
        qs = BlogPost.objects.filter(title=title)
        if instance is not None:
            qs = qs.exclude(pk=instance.pk)
        if qs.exists():
            raise forms.ValidationError("This title already exists. Please try again")
        return title
    
    """ def clean_publish_date(self, *args, **kwars):
        date = self.cleaned_data.get('publish_date')
        now  = timezone.now().isoformat()
        if date.
        
 """
