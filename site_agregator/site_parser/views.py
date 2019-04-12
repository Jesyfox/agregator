from django.shortcuts import render

from . import parsers
from .models import Post


def habr_parser_starter(request):
    site = 'https://habr.com'
    parser_habr = parsers.Habr()
    context = {'models_count': Post.objects.filter(site_url__url=site).count(),
               'site': site}
    if request.method == 'POST':
        parser_habr.start_parse()
    return render(request, 'parser_starter.html', context=context)
