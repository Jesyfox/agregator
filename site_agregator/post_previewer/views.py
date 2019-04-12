from django.shortcuts import render, get_object_or_404
from django.views.generic import View

from site_parser.models import Post


class Index(View):
    template_name = 'index.html'
    data = {'posts': Post.objects.all()}

    def get(self, request):
        return render(request, self.template_name, context=self.data)


class PostDetail(View):
    template_name = 'post_detail.html'

    def get(self, request, pk):
        data = {'post': get_object_or_404(Post, pk=pk)}
        return render(request, self.template_name, context=data)
