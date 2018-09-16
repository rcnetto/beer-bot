# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class HomeBrewItem(scrapy.Item):
    # define the fields for your item here like:
    id = scrapy.Field()
    nome = scrapy.Field()
    categoria = scrapy.Field()
    preco = scrapy.Field()
    url = scrapy.Field()
    last_updated = scrapy.Field(serializer=str)
    pass
