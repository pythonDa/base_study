# -*- coding: utf-8 -*-
import scrapy
from scrapy_splash import SplashRequest

class GuaziSpider(scrapy.Spider):
    name = 'guazi'
    allowed_domains = ['guazi.com']

    def start_requests(self):
        url = 'https://www.guazi.com/suihua/buy/'
        yield SplashRequest(url, callback=(self.parse), args={'wait': 1})

    def parse(self, response):
        print(response.text)