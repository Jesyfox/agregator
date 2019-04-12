from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return f'{self.name}'


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
    tags = models.ManyToManyField(Tag)
    body_content = models.TextField()

    def __str__(self):
        return f'{self.title}'
