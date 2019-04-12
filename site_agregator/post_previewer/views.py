from django.shortcuts import render
from django.views.generic import View

from site_parser.models import Post


class Index(View):
    template_name = 'index.html'
    data = {'posts': Post.objects.all()}

    def get(self, request):
        return render(request, self.template_name, context=self.data)
