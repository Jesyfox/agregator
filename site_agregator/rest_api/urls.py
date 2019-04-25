from django.urls import path, include

from rest_framework import routers
from rest_framework_swagger.views import get_swagger_view

from . import api_views


router = routers.DefaultRouter()
router.register(r'posts', api_views.PostViewSet)
router.register(r'tags', api_views.TagViewSet)

schema_view = get_swagger_view(title='Site agregator')

urlpatterns = [
    path('api/', include((router.urls, 'site_parser'))),
    path('api/swagger/', schema_view),
    path('api/posts/<int:pk>/body/', api_views.PostBody.as_view(), name='posts-body'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]