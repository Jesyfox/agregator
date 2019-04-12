from django.urls import path

from . import views

urlpatterns = [
    path('parse/habr/', views.habr_parser_starter, name='parser_starter'),
]
