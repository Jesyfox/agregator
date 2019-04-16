from django.contrib import admin

from .models import Post, Author, SiteUrl

admin.site.register(Post)
admin.site.register(Author)
admin.site.register(SiteUrl)
