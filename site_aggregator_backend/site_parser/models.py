from django.db import models

from tagging.registry import register as tag_register


class SiteUrl(models.Model):
    url = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.url}'


class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name}'


class Post(models.Model):
    site_url = models.ForeignKey(SiteUrl, on_delete=models.CASCADE)
    post_url = models.URLField(unique=True)
    title = models.CharField(max_length=300)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    body_content = models.TextField()

    def __str__(self):
        return f'{self.site_url} {self.title}'


tag_register(Post)
