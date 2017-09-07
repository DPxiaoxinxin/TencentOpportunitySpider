# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TencentItem(scrapy.Item):
    name = scrapy.Field()
    type = scrapy.Field()
    hire_count = scrapy.Field()
    local = scrapy.Field()
    pub_time = scrapy.Field()
    href = scrapy.Field()
    responsibilities = scrapy.Field()
    requirements = scrapy.Field()
