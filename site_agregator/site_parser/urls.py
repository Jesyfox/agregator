from django.urls import path

from . import views

urlpatterns = [
    path('habr/', views.HabrStarter.as_view(), name='habr_parser_starter'),
    path('tproger_python/', views.TprogerPythonStarter.as_view(), name='tproger_python_parser_starter'),
]
