from django.urls import path

from . import views

urlpatterns = [
    path('habr/', views.habr_parser_starter, name='habr_parser_starter'),
    path('tproger_python/', views.tproger_python_parser_starter, name='tproger_python_parser_starter'),
]
