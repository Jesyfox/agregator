from django.db.utils import IntegrityError

import logging
import requests
import lxml.html as html
import time

from . import utils
from .models import Post

logger = logging.getLogger('parser')


def add_post_to_db(data):
    new_post = Post(site_url=utils.get_site_url_object(data['site_url']),
                    post_url=data['post_url'],
                    title=data['title'],
                    author=utils.get_author_object(data['author']),
                    body_content=data['body_content']
                    )
    try:
        new_post.save()
    except IntegrityError:
        pass
    else:
        new_post.tags = ','.join(data['tags']).lower()
        logger.info(f'new_post: {data["title"]}')


class Parser:
    PARSER = {}
    field_mappings = {
        'title': '_get_title',
        'tags': '_get_tags_list',
        'author': '_get_author',
        'body_content': '_get_body_content'
    }

    site_url = ''

    @staticmethod
    def get_tree_element(response, base_url=None):
        return html.fromstring(response.content.decode('UTF-8'), base_url=base_url)

    def __init__(self):
        if not self.site_url:
            raise NotImplementedError('You must overwrite site_url var')

        try:
            response = requests.get(self.site_url, timeout=20)
        except requests.exceptions.Timeout:
            logger.error(f'main url {self.site_url}, timed out!')
        else:
            self.page_tree = self.get_tree_element(response)

    def _get_post_list(self, page_tree):
        raise NotImplementedError

    def _get_page_list(self):
        """
        :return: [self.page_tree,(!!!) '*page_url*/page2/', '*page_url*/page3/', '*page_url*/page4/']
        """
        raise NotImplementedError

    def _get_tags_list(self, post_tree):
        raise NotImplementedError

    def _get_title(self, post_tree):
        raise NotImplementedError

    def _get_author(self, post_tree):
        raise NotImplementedError

    def _get_body_content(self, post_tree):
        raise NotImplementedError

    def tree_iterator(self, url_list):
        for url in url_list:
            logger.debug(f'get url {url}')
            try:
                response = requests.get(url, timeout=20)
                time.sleep(3)
            except requests.exceptions.Timeout:
                logger.error(f'url {url}, timed out!')
            else:
                tree = self.get_tree_element(response, base_url=url)
                logger.debug('yielding tree')
                yield tree

    def parse_data_from_post(self, post_tree):
        data = {'site_url': self.site_url}
        logger.debug('parsing data from post...')
        for field_key in self.field_mappings.keys():
            try:
                logger.debug(f'getting field key {field_key}')
                field = getattr(self, self.field_mappings[field_key])
                data.update({field_key: field(post_tree)})
                logger.debug('field key added')
            except Exception as e:
                logger.error(e)
                continue
        data.update({'post_url': post_tree.base})
        logger.debug('page_parsing done!')
        return data

    def start_parse(self):
        logger.debug('start parse...')
        for page_tree in self.tree_iterator(self._get_page_list()):
            for post_tree in self.tree_iterator(self._get_post_list(page_tree)):
                data = self.parse_data_from_post(post_tree)
                add_post_to_db(data)
        logger.debug('parse is done!')

    @classmethod
    def register(cls, name):
        def dec(parser_cls):
            cls.PARSER[name] = parser_cls
            return parser_cls
        return dec

    @classmethod
    def get(cls, name, **kwargs):
        return cls.PARSER[name](**kwargs)


@Parser.register('habr')
class Habr(Parser):
    site_url = 'https://habr.com'

    def _get_post_list(self, page_tree):
        xpath = '//a[@class="post__title_link"]/@href'
        res = page_tree.xpath(xpath)
        return res

    def _get_page_list(self):
        xpath = '//a[@class="toggle-menu__item-link toggle-menu__item-link_pagination"]/@href'
        page_list = [self.site_url, ] + [self.site_url + page_url for page_url in self.page_tree.xpath(xpath)]
        return page_list

    def _get_title(self, post_tree):
        xpath = '//span[@class="post__title-text"]/text()'
        res = post_tree.xpath(xpath)[0]
        return res

    def _get_tags_list(self, post_tree):
        xpath = '//a[@class="inline-list__item-link post__tag  "]/text()'
        res = post_tree.xpath(xpath)
        return res

    def _get_author(self, post_tree):
        xpath = '//span[@class="user-info__nickname user-info__nickname_small"]/text()'
        res = post_tree.xpath(xpath)[0]
        return res

    def _get_body_content(self, post_tree):
        xpath = '//div[@class="post__body post__body_full"]'
        element = post_tree.xpath(xpath)
        content = html.tostring(element[0], encoding='unicode')
        return content


@Parser.register('tproger-python')
class TProgerPython(Parser):
    site_url = 'https://tproger.ru/tag/python/'

    def _get_post_list(self, page_tree):
        xpath = '//div[@class="entry-image"]/a/@href'
        res = page_tree.xpath(xpath)
        return res

    def _get_page_list(self):
        xpath = '//div[@class="pagination"]/a/@href'
        return self.page_tree.xpath(xpath)

    def _get_title(self, post_tree):
        xpath = '//h1[@class="entry-title"]/text()'
        res = post_tree.xpath(xpath)[0]
        return res

    def _get_tags_list(self, post_tree):
        xpath = '//footer[@class="entry-meta clearfix"]/ul/li/a/text()'
        res = post_tree.xpath(xpath)
        return res

    def _get_author(self, post_tree):
        xpath = '//div[@class="post-meta "]/ul/li/a/text()'
        res = post_tree.xpath(xpath)[0]
        return res

    def _get_body_content(self, post_tree):
        xpath = '//div[@class="entry-content"]'
        element = post_tree.xpath(xpath)
        content = html.tostring(element[0], encoding='unicode')
        return content
