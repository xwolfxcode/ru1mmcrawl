# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class RuyiItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    urlid = scrapy.Field()
    dpath = scrapy.Field()
    cover = scrapy.Field()
