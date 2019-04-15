from django.shortcuts import render, get_object_or_404
from django.views.generic.list import ListView
from django.views.generic import View
from django.core.exceptions import ImproperlyConfigured

from tagging.views import TaggedObjectList

from site_parser.models import Post


class PostTagDetail(TaggedObjectList):
    model = Post
    paginate_by = 20
    template_name = 'post_list.html'

    def get_queryset_or_model(self):
        query = self.request.GET.get('q')
        if query:
            return Post.objects.filter(title__icontains=query)
        elif self.model is not None:
            return self.model
        else:
            raise ImproperlyConfigured(
                "%(cls)s is missing a QuerySet. Define "
                "%(cls)s.model, %(cls)s.queryset, or override "
                "%(cls)s.get_queryset_or_model()." % {
                    'cls': self.__class__.__name__
                }
            )


class PostListView(ListView):
    model = Post
    paginate_by = 20
    template_name = 'post_list.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return Post.objects.filter(title__icontains=query)
        else:
            return Post.objects.all()


class PostDetail(View):
    template_name = 'post_detail.html'

    def get(self, request, pk):
        data = {'post': get_object_or_404(Post, pk=pk)}
        return render(request, self.template_name, context=data)
