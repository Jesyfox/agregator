from .models import SiteUrl, Author


def get_author_object(author):
    return Author.objects.get_or_create(name=author)[0]


def get_site_url_object(site_url):
    return SiteUrl.objects.get_or_create(url=site_url)[0]
