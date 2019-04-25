from rest_framework import serializers
from tagging.models import Tag, TaggedItem

from site_parser.models import SiteUrl, Author, Post


class SiteUrlPostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SiteUrl
        fields = ('id', 'url', )


class AuthorPostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Author
        fields = ('id', 'name', )


class TagPostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tag
        fields = ('id', 'name', )


class PostSerializer(serializers.HyperlinkedModelSerializer):
    site_url = SiteUrlPostSerializer()
    author = AuthorPostSerializer()
    tags = TagPostSerializer(many=True)
    body = serializers.HyperlinkedIdentityField(
        view_name='rest_api:posts-body', format='html')

    class Meta:
        model = Post
        fields = ('id', 'site_url', 'title', 'post_url',
                  'tags', 'body', 'author')


class TaggedPostSerializer(serializers.HyperlinkedModelSerializer):
    site_url = SiteUrlPostSerializer()

    class Meta:
        model = Post
        fields = ('id', 'title', 'site_url')


class TaggedItemSerializer(serializers.HyperlinkedModelSerializer):
    object = TaggedPostSerializer()

    class Meta:
        model = TaggedItem
        fields = ('object',)


class TagSerializer(serializers.HyperlinkedModelSerializer):
    posts = TaggedItemSerializer(many=True, source='items')

    class Meta:
        model = Tag
        fields = ('id', 'name', 'posts')
