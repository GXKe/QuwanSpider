# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
from scrapy.http import Request
import time


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
        self.item = 0
        for p  in products:
            count +=  1
            print ("==========首页：%d===========" % count)
            print ("title : " + p.xpath('dl/dd/a/@title').extract()[0])
            print("link : " + p.xpath('dl/dd/a/@href').extract()[0])
            print("price : " + p.xpath('dl/dd/span/text()').extract()[0])
            print("logo : " + p.xpath('a/img[@onerror="imgerror(event)"]/@src').extract()[0])
            url = p.xpath('dl/dd/a/@href').extract()[0]
            print("link : " + url)

            site = "http://www.quwan.com/"
            if url.find(site) == -1:
                url = site + url
            print("生成抓取任务：" + url)
            yield Request(url=url, callback=self.parse_details, meta={'url': url})
        print("抓取产品列表总数：%d" % count)


    def parse_details(self, response):
        self.item+=1;
        print("item idx: %d" % self.item)
        print("抓取到详情页url：" + response.meta['url'])
        #time.sleep(1)

        #解析产品详情
        sel = Selector(response)

        print("缩略大图1  href")
        imgs = sel.xpath('//a[@class ="cloud-zoom"]/@href').extract()
        for img in imgs:
            print(img)

        print("缩略大图2 src")
        imgs = sel.xpath('//a[@class ="cloud-zoom"]/img/@src').extract()
        for img in imgs:
            print(img)

        print("缩略小图 src")
        imgs = sel.xpath('//ul[@class="pic_index"]/li[@class="pic_li"]/img/@src').extract()
        for img in imgs:
            print(img)

        print("资源详情图")
        imgs = sel.xpath('//div[@class="box details"]/p/img/@src').extract()
        for img in imgs:
            print(img)