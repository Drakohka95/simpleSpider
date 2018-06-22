# -*- coding: utf-8 -*-

import scrapy


class InfaItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    body = scrapy.Field()
    date = scrapy.Field()
    pass
