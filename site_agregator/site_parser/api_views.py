from rest_framework import viewsets
from tagging.models import Tag, TaggedItem

from .models import SiteUrl, Author, Post
from .serializers import SiteUrlSerializer, AuthorSerializer, TagSerializer, PostSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
