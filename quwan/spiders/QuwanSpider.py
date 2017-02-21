# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
from scrapy.http import Request
import re
from quwan.items import  QuwanItem


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

            urlid = re.compile(r'//.*/(.*?)\.html').findall(url)[0]
            print("=====生成抓取任务："+ urlid + url)
            yield Request(url=url, callback=self.parse_details, meta={'url': url, 'urlid':urlid})
        print("=====抓取产品列表总数：%d" % count)


    def parse_details(self, response):
        self.item+=1;
        item = QuwanItem()
        print("item idx: %d" % self.item)
        print("=====抓取到详情页url：" + response.meta['url'])
        print("=====商品id：" + response.meta['urlid'])
        item['page_id'] = "home_index"
        item['goods_id'] = response.meta['urlid']


        #解析产品详情
        sel = Selector(response)

        print("=====缩略大图1  href")
        imgs = sel.xpath('//a[@class ="cloud-zoom"]/@href').extract()
        for img in imgs:
            print(img)
        item['pic_zoom_b1'] = imgs

        print("=====缩略大图2 src")
        imgs = sel.xpath('//a[@class ="cloud-zoom"]/img/@src').extract()
        for img in imgs:
            print(img)
        item['pic_zoom_b2'] = imgs

        print("=====缩略小图 src")
        imgs = sel.xpath('//ul[@class="pic_index"]/li[@class="pic_li"]/img/@src').extract()
        for img in imgs:
            print(img)
        item['pic_zoom_m'] = imgs

        print("=====资源详情图")
        imgs = sel.xpath('//div[@class="box details"]/p/img/@src').extract()
        for img in imgs:
            print(img)
        item['pic_des'] = imgs

        print("=====商品介绍")
        imgs = sel.xpath('//div[@class="gn_decri"]/p/text()').extract()
        for img in imgs:
            print(img)
        item['goods_des'] = imgs[0]

        print("=====商品参数名")
        imgs = sel.xpath('//ul[@class="csList"]/li/b/text()').extract()
        for img in imgs:
            print(img)
        item['params_name'] = imgs

        print("=====商品参数值")
        imgs = sel.xpath('//ul[@class="csList"]/li/text()').extract()
        for img in imgs:
            print(img)
        item['params_val'] = imgs

        print("=====品牌")
        imgs = sel.xpath('//div[@id="paykey_new"]//ul/li/dl/dd/a/text()').extract()
        #for img in imgs:
         #   print(imgs)
        print(imgs[0])
        item['brand'] = imgs[0]

        print("=====价格")
        imgs = sel.xpath('//dt[@id="price_goods_div"]/strong/text()').extract()
        for img in imgs:
            print(img)
        item['price'] = imgs[0]

        print("=====名称")
        imgs = sel.xpath('//div[@class="infor"]/h1/text()').extract()
        for img in imgs:
            print(img)
        item['title'] = imgs[0]
        yield item;