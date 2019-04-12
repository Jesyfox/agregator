from django.urls import path

from . import views

urlpatterns = [
    path('start/', views.parser_starter, name='parser_starter'),
]
