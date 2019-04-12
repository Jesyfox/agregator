import requests
import lxml.etree as et

try:
    import utils
except ModuleNotFoundError:
    from . import utils


class Parser:
    field_mappings = {
        'title': '_get_title',
        'tags': '_get_tags_list',
        'author': '_get_author',
        'body_content': '_get_body_content'
    }

    site_url = ''

    def __init__(self):
        if not self.site_url:
            raise NotImplementedError('You must overwrite site_url var')

        page = requests.get(self.site_url)
        self.page_tree = et.HTML(page.content)

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

    @staticmethod
    def tree_iterator(url_list):
        for url in url_list:
            r_url = requests.get(url)
            tree = et.HTML(r_url.content, base_url=url)
            yield tree

    def parse_data_from_post(self, post_tree):
        data = {'site_url': self.site_url}
        for field_key in self.field_mappings.keys():
            field = getattr(self, self.field_mappings[field_key])
            data.update({field_key: field(post_tree)})
        data.update({'post_url': post_tree.base})
        return data

    def start_parse(self):
        for page_tree in self.tree_iterator(self._get_page_list()):
            for post_tree in self.tree_iterator(self._get_post_list(page_tree)):
                data = self.parse_data_from_post(post_tree)
                utils.add_post_to_db(data)


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
        res = post_tree.xpath(xpath)
        return res

    def _get_tags_list(self, post_tree):
        xpath = '//a[@class="inline-list__item-link post__tag  "]/text()'
        res = post_tree.xpath(xpath)
        return res

    def _get_author(self, post_tree):
        xpath = '//span[@class="user-info__nickname user-info__nickname_small"]/text()'
        res = post_tree.xpath(xpath)
        return res

    def _get_body_content(self, post_tree):
        xpath = '//div[@class="post__body post__body_full"]'
        element = post_tree.xpath(xpath)
        content = et.tostring(element[0], encoding='unicode')
        return content


if __name__ == '__main__':
    test = Habr()
    test.start_parse()
