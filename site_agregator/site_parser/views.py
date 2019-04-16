from django.shortcuts import render

from .models import Post
from .tasks import parse


def habr_parser_starter(request):
    site = 'https://habr.com'
    context = {'models_count': Post.objects.filter(site_url__url=site).count(),
               'site': site}
    if request.method == 'POST':
        parse.delay('habr')
    return render(request, 'parser_starter.html', context=context)


def tproger_python_parser_starter(request):
    site = 'https://tproger.ru/tag/python/'
    context = {'models_count': Post.objects.filter(site_url__url=site).count(),
               'site': site}
    if request.method == 'POST':
        parse.delay('tproger-python')
    return render(request, 'parser_starter.html', context=context)