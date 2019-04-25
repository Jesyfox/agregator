from django.urls import path

from . import views

urlpatterns = [
    path('parse/habr/', views.HabrStarter.as_view(), name='habr_parser_starter'),
    path('parse/tproger_python/', views.TprogerPythonStarter.as_view(), name='tproger_python_parser_starter'),
]