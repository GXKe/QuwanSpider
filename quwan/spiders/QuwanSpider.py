# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector


class QuwanspiderSpider(scrapy.Spider):
    name = "QuwanSpider"
    allowed_domains = ["quwan.com"]
    start_urls = (
        'http://www.quwan.com/',
    )

    def parse(self, response):
        sel = Selector(response)
        products = sel.xpath( "//div[@class='brick col1 commodity bestlikes masonry-brick']")
        #print("商品数量：%d" % products.count())
        for p  in products:
            print (p.xpath('a/@title').extract())
