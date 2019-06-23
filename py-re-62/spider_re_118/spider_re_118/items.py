# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class SpiderRe118Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title=scrapy.Field()
    href = scrapy.Field()
    position=scrapy.Field()
    num=scrapy.Field()
    price=scrapy.Field()
    broker=scrapy.Field()
    style=scrapy.Field()
    ting =scrapy.Field()
    size =scrapy.Field()
    direction =scrapy.Field()
