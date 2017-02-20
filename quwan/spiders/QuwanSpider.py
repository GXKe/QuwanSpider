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
        count = 0;
        for p  in products:
            count +=  1
            print ("==========%d===========" % count)
            print ("title : " + p.xpath('dl/dd/a/@title').extract()[0])
            print("link : " + p.xpath('dl/dd/a/@href').extract()[0])
            print("price : " + p.xpath('dl/dd/span/text()').extract()[0])
            print("logo : " + p.xpath('a/img[@onerror="imgerror(event)"]/@src').extract()[0])
            print("link : " + p.xpath('dl/dd/a/@href').extract()[0])
        print("抓取总数：%d" % count)