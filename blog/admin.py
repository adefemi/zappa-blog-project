from django.contrib import admin
from .models import (BlogTagModel, BlogModel, BlogCommentModel)


admin.site.register(
	(BlogTagModel, BlogModel, BlogCommentModel)
)
