from __future__ import absolute_import, unicode_literals
from celery import shared_task

from .parsers import Parser


@shared_task
def parse(parser_name):
    parser = Parser.get(parser_name)
    parser.start_parse()
