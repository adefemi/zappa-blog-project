from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (BlogView, BlogTagView, BlogCommentView, TopBlogView, SimilarBlogView)


router = DefaultRouter()
router.register('blogs', BlogView, basename='blog_list')
router.register('blogs-tags', BlogTagView, basename='blog_tag_list')
router.register('blogs-comments', BlogCommentView, basename='blog_comment_list')
router.register('top-blogs', TopBlogView, basename='top_blog_list')
router.register('similar-blogs', SimilarBlogView, basename='similar_blog_list')

urlpatterns = [
	path('', include(router.urls)),
]
