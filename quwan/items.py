# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class QuwanItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    goods_id = scrapy.Field()   #商品id
    page_id = scrapy.Field()    #商品索引页
    logo = scrapy.Field()       #商品列表logo
    price = scrapy.Field()
    title = scrapy.Field()
    brand = scrapy.Field()  #品牌

    pic_zoom_b1 = scrapy.Field() #缩略大图1
    pic_zoom_b2 = scrapy.Field() #缩略大图2
    pic_zoom_m = scrapy.Field()  #缩略小图

    pic_des  = scrapy.Field() #商品详情图
    goods_des = scrapy.Field() #商品文本简介

    params_name = scrapy.Field()    #参数
    params_val = scrapy.Field()


