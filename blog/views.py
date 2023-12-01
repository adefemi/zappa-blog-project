from rest_framework.viewsets import ModelViewSet
from blog_project.utils import (Helper, get_query)
from .models import (BlogModel, BlogCommentModel, BlogTagModel)
from .serializers import (BlogSerializer, BlogCommentSerializer, BlogTagSerializer)
from django.db.models import (Count, Q)


class BlogView(ModelViewSet):
	queryset = BlogModel.objects.all()
	serializer_class = BlogSerializer
	lookup_field = 'slug'

	def get_queryset(self):
		if self.request.method.lower() != 'get':
			return self.queryset

		params = self.request.query_params.dict()
		keyword = params.pop('keyword', None)
		params.pop('page', None)
		results = self.queryset.filter(**params)
		if keyword:
			search_fields = ['title', 'tag__title']
			query = get_query(keyword, search_fields)
			results = results.filter(query)

		return results


class BlogCommentView(ModelViewSet):
	queryset = BlogCommentModel.objects.all()
	serializer_class = BlogCommentSerializer


class BlogTagView(ModelViewSet):
	queryset = BlogTagModel.objects.all()
	serializer_class = BlogTagSerializer


class TopBlogView(ModelViewSet):
	queryset = BlogModel.objects.all()
	serializer_class = BlogSerializer
	http_method_names = ['get']

	def get_queryset(self):
		results = self.queryset.annotate(blog_comments_count=Count('blog_comments')).order_by('-blog_comments_count')[:5]

		return results


class SimilarBlogView(ModelViewSet):
	queryset = BlogModel.objects.all()
	serializer_class = BlogSerializer
	http_method_names = ['get']

	def get_queryset(self):
		blog_id = self.kwargs.get('blog_id')
		try:
			items = self.queryset.get(id=blog_id).tags.all()
		except Exception as e:
			self.queryset = None
		if self.queryset is not None:
			self.queryset = self.queryset.filter(tags__id__in=[a.id for a in items]).exclude(id=blog_id)
		results = self.queryset

		return results
