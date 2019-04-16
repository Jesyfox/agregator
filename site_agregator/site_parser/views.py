from django.shortcuts import render
from django.views.generic import View

from .models import Post
from .tasks import parse


class ParserView(View):
    site = ''
    parser = ''
    template_name = 'parser_starter.html'

    def __init__(self):
        super().__init__()
        self.context = {'models_count': Post.objects.filter(site_url__url=self.site).count(),
                        'site': self.site}

    def get(self, request):
        return render(request, self.template_name, context=self.context)

    def post(self, request):
        parse.delay(self.parser)
        return render(request, self.template_name, context=self.context)


class HabrStarter(ParserView):
    site = 'https://habr.com'
    parser = 'habr'


class TprogerPythonStarter(ParserView):
    site = 'https://tproger.ru/tag/python/'
    parser = 'tproger-python'
