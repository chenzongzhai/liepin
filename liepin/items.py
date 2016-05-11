# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class LiepinItem(scrapy.Item):
    # define the fields for your item here like:
    url = scrapy.Field()
    name = scrapy.Field()
    company_name = scrapy.Field()
    company_size = scrapy.Field()
    company_address = scrapy.Field()
    company_type = scrapy.Field()
    pay = scrapy.Field()
    publish_time = scrapy.Field()
    requires = scrapy.Field()
