from django.urls import path

from . import views

urlpatterns = [
    path('', views.PostListView.as_view(), name='post_list'),
    path('<int:pk>', views.PostDetail.as_view(), name='post_detail')
]
