from rest_framework import serializers
from .models import (BlogTagModel, BlogModel, BlogCommentModel)


class BlogTagSerializer(serializers.ModelSerializer):
	class Meta:
		model = BlogTagModel
		fields = ['id', 'title']


class BlogSerializer(serializers.ModelSerializer):
	tag = BlogTagSerializer(read_only=True)
	tag_id = serializers.IntegerField(write_only=True)
	class Meta:
		model = BlogModel
		fields = '__all__'


class BlogCommentSerializer(serializers.ModelSerializer):
	blog = BlogSerializer(read_only=True)
	blog_id = serializers.IntegerField(write_only=True)
	class Meta:
		model = BlogCommentModel
		fields = '__all__'
