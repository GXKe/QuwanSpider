# -*- coding: utf-8 -*-
import scrapy


class QuwanspiderSpider(scrapy.Spider):
    name = "QuwanSpider"
    allowed_domains = ["quwan.com"]
    start_urls = (
        'http://www.quwan.com/',
    )

    def parse(self, response):
        pass
