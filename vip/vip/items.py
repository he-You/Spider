# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class VipItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # name = scrapy.Field()           # 标题
    # price = scrapy.Field()          # 价格
    # brand = scrapy.Field()          # 品牌
    # category = scrapy.Field()       # 类目
    # market_price = scrapy.Field()   # 市场价
    # vip_discount = scrapy.Field()   # 打折

    title = scrapy.Field()
    link = scrapy.Field()
    price = scrapy.Field()
    comment = scrapy.Field()