from django.db import models
from django.utils.text import slugify


class BlogTagModel(models.Model):
	title = models.CharField(unique=True, max_length=50)
	created_at = models.DateTimeField(auto_now_add=True)



class BlogModel(models.Model):
	tag = models.ForeignKey('BlogTagModel', on_delete=models.CASCADE, related_name='blogs')
	cover = models.ImageField(null=True, blank=True)
	title = models.CharField(unique=True, max_length=255)
	slug = models.SlugField(unique=True, default='', editable=False, max_length=255)
	author = models.CharField(default='Annoymous', max_length=255)
	content = models.TextField()
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	class Meta:
		ordering = ('-created_at', )
	def save(self, *args, **kwargs):
		self.slug = slugify(self.title, allow_unicode=True)
		super().save(*args, **kwargs)


class BlogCommentModel(models.Model):
	blog = models.ForeignKey('BlogModel', on_delete=models.CASCADE, related_name='blog_comments')
	author = models.CharField(default='Annoymous', max_length=255)
	ip = models.CharField(null=True, blank=True, max_length=50)
	comment = models.TextField()
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	class Meta:
		ordering = ('-created_at',)
