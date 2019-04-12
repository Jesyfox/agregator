from django.db.utils import IntegrityError
from .models import Post, Tag, SiteUrl, Author


def get_author_object(author):
    return Author.objects.get_or_create(name=author)[0]


def get_site_url_object(site_url):
    return SiteUrl.objects.get_or_create(url=site_url)[0]


def get_tag_object(tag):
    return Tag.objects.get_or_create(name=tag)[0]


def add_post_to_db(data):
    print('data:')
    for k, i in data.items():
        if k != 'body_content':
            print(f'\t{k} --> {i}')
        else:
            print(f'\t{k} --> {len(i)}')

    new_post = Post(site_url=get_site_url_object(data['site_url']),
                    post_url=data['post_url'],
                    title=data['title'],
                    author=get_author_object(data['author']),
                    body_content=data['body_content']
                    )
    try:
        new_post.save()
    except IntegrityError:
        pass
    else:
        [new_post.tags.add(get_tag_object(tag)) for tag in data['tags']]
