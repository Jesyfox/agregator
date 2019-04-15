from django.shortcuts import render, get_object_or_404
from django.views.generic.list import ListView
from django.views.generic import View

from tagging.models import TaggedItem

from site_parser.models import Post


class PostListView(ListView):
    model = Post
    paginate_by = 20
    template_name = 'post_list.html'

    def get_context_data(self, **kwargs):
        context = super(ListView, self).get_context_data(**kwargs)
        return context

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return TaggedItem.objects.get_by_model(Post, query)  # ['house', 'thing'])
        else:
            return Post.objects.all()


class PostDetail(View):
    template_name = 'post_detail.html'

    def get(self, request, pk):
        data = {'post': get_object_or_404(Post, pk=pk)}
        return render(request, self.template_name, context=data)
