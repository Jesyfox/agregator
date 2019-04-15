from django.urls import path, re_path

from tagging.views import TaggedObjectList
from site_parser.models import Post

from . import views

urlpatterns = [
    path('', views.PostListView.as_view(), name='post_list'),
    path('<int:pk>', views.PostDetail.as_view(), name='post_detail'),
    path('tag/<str:tag>', views.PostTagDetail.as_view(), name='post_tag_detail')
]
