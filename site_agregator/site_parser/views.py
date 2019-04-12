from django.shortcuts import render

from . import parsers


def parser_starter(request):
    parser_habr = parsers.Habr()
    if request.method == 'POST':
        parser_habr.start_parse()
    return render(request, 'parser_starter.html')
