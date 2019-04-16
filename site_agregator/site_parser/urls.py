from django.urls import path, include

from rest_framework import routers

from . import views
from . import api_views

urlpatterns = [
    path('parse/habr/', views.HabrStarter.as_view(), name='habr_parser_starter'),
    path('parse/tproger_python/', views.TprogerPythonStarter.as_view(), name='tproger_python_parser_starter'),
]

router = routers.DefaultRouter()
router.register(r'posts', api_views.PostViewSet)
router.register(r'tags', api_views.TagViewSet)

urlpatterns += [
    path('api/', include((router.urls, 'site_parser'))),
    path('api/posts/<int:pk>/body/', api_views.PostBody.as_view(), name='posts-body'),
]
