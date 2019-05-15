# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class SpiderRe77Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    pass
#函數要加Item才給用
class USdramaItem(scrapy.Item):
    name = scrapy.Field()
    href = scrapy.Field()
    tv = scrapy.Field()
    state = scrapy.Field()
    time = scrapy.Field()
