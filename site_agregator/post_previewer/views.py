from django.shortcuts import render, get_object_or_404
from django.views.generic.list import ListView
from django.views.generic import View

from tagging.views import TaggedObjectList

from site_parser.models import Post


class PostTagDetail(TaggedObjectList):
    model = Post
    paginate_by = 20
    template_name = 'post_list.html'


class PostListView(ListView):
    model = Post
    paginate_by = 20
    template_name = 'post_list.html'

    def get_context_data(self, **kwargs):
        context = super(ListView, self).get_context_data(**kwargs)
        return context


class PostDetail(View):
    template_name = 'post_detail.html'

    def get(self, request, pk):
        data = {'post': get_object_or_404(Post, pk=pk)}
        return render(request, self.template_name, context=data)
