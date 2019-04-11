import requests

import lxml.etree as et


class Parser:
    field_mappings = {
        'url': '_get_url',
        'title': '_get_title',
        'tags': '_get_tags',
        'author': '_get_author',
        'body_content': '_get_body_content'
    }

    def __init__(self, site_url):

        self.site_url = site_url

        page = requests.get(self.site_url)
        self.page_tree = et.HTML(page.content)

    def _get_post_list(self, page_tree):
        post_url_list = []
        if not post_url_list:
            raise NotImplementedError

        post_tree_list = []

        for post_url in post_url_list:
            r_post = requests.get(post_url)
            post_tree = et.HTML(r_post.content, base_url=post_url)
            post_tree_list.append(post_tree)

        for post_tree in post_tree_list:
            yield post_tree

    def _get_page_tree_list(self):
        """
        :return: [self.page_tree, '*page_url*/ru/page2/', '*page_url*/ru/page3/', '*page_url*/ru/page4/']
        """
        page_tree_list = [self.page_tree, ]

        # xPath add

        return page_tree_list

    def _get_url(self, tree):
        return tree.base

    def _get_title(self, tree):
        raise NotImplementedError

    def _get_tags(self, tree):
        raise NotImplementedError

    def _get_author(self, tree):
        raise NotImplementedError

    def _get_body_content(self, tree):
        raise NotImplementedError

    def update_db(self, data):
        pass  # !!!!!!!!!

    def start_parse(self):
        data = {'site': self.site_url}
        for page_tree in self._get_page_tree_list():
            for post_tree in self._get_post_list(page_tree):
                for field_key in self.field_mappings.keys():
                    field = getattr(self, self.field_mappings[field_key])
                    data.update({field_key: field(post_tree)})
                self.update_db(data)
                data = {'site': self.site_url}
