from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=40)


class SiteUrl(models.Model):
    url = models.URLField()


class Author(models.Model):
    name = models.CharField(max_length=100)


class Post(models.Model):
    site_url = models.ForeignKey(SiteUrl, on_delete=models.CASCADE)
    post_url = models.URLField(unique=True)
    title = models.CharField(max_length=300)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)
    body_content = models.TextField()
