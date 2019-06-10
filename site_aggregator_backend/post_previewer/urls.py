from django.urls import path

from . import views

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('posts/', views.PostListView.as_view(), name='post_list'),
    path('posts/<int:pk>', views.PostDetail.as_view(), name='post_detail'),
    path('tags/', views.TagList.as_view(), name='tag_list'),
    path('tags/<int:tag>', views.PostTagDetail.as_view(), name='post_tag_detail')
]
