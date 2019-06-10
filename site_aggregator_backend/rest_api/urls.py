from django.urls import path, include

from rest_framework import routers, permissions

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from . import api_views


router = routers.DefaultRouter()
router.register(r'posts', api_views.PostViewSet)
router.register(r'tags', api_views.TagViewSet)

urlpatterns = [
    path('api/', include((router.urls, 'site_parser'))),
    path('api/posts/<int:pk>/body/', api_views.PostBody.as_view(), name='posts-body'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]

schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns += [
   path('api/swagger<format>', schema_view.without_ui(cache_timeout=0), name='schema-json'),
   path('api/swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   path('api/redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
