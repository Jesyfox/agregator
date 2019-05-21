from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.list import ListView
from django.views.generic import View
from django.core.exceptions import ImproperlyConfigured
from django.db.models.query import QuerySet

from tagging.views import TaggedObjectList
from tagging.models import Tag

from site_parser.models import Post


class Index(View):
    template_name = 'index.html'

    def get(self, request):
        return render(request, self.template_name)


class TagList(ListView):
    model = Tag
    template_name = 'tag_list.html'

    def get_queryset(self):
        if self.queryset is not None:
            queryset = self.queryset
            if isinstance(queryset, QuerySet):
                queryset = queryset.all()
        elif self.model is not None:
            queryset = self.model.objects.usage_for_model(Post, counts=True, min_count=2)
        else:
            raise ImproperlyConfigured(
                "%(cls)s is missing a QuerySet. Define "
                "%(cls)s.model, %(cls)s.queryset, or override "
                "%(cls)s.get_queryset()." % {
                    'cls': self.__class__.__name__
                }
            )
        ordering = self.get_ordering()
        if ordering:
            if isinstance(ordering, str):
                ordering = (ordering,)
            queryset = queryset.order_by(*ordering)

        return queryset


class PostTagDetail(TaggedObjectList):
    model = Post
    paginate_by = 15
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
    paginate_by = 15
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
