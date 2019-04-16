from rest_framework import serializers
from tagging.models import Tag, TaggedItem

from .models import SiteUrl, Author, Post


class SiteUrlSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SiteUrl
        fields = ('id', 'url', )


class AuthorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Author
        fields = ('id', 'name', )


class TagSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tag
        fields = ('id', 'name', )


class PostSerializer(serializers.HyperlinkedModelSerializer):
    site_url = SiteUrlSerializer()
    author = AuthorSerializer()
    tags = TagSerializer(many=True)

    class Meta:
        model = Post
        fields = ('id', 'site_url', 'title', 'post_url', 'tags', 'author')
