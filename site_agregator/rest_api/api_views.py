from rest_framework import viewsets, generics, renderers
from rest_framework.response import Response

from tagging.models import Tag

from site_parser.models import Post
from .serializers import TagSerializer, PostSerializer

import rest_framework_swagger

class PostBody(generics.GenericAPIView):
    """
    get:
    Return body content in html lang of the given post.

    """
    queryset = Post.objects.all()
    renderer_classes = (renderers.StaticHTMLRenderer,)

    def get(self, request, *args, **kwargs):
        post = self.get_object()
        return Response(post.body_content)


class PostViewSet(viewsets.ReadOnlyModelViewSet):
    """
    retrieve:
    Return the given post.

    list:
    Return a list of all the existing posts.

    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class TagViewSet(viewsets.ReadOnlyModelViewSet):
    """
    retrieve:
    Return the given tag.

    list:
    Return a list of all the existing tags.

    """
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
