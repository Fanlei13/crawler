# -*- coding: utf-8 -*-
from scrapy.linkextractors.lxmlhtml import LxmlLinkExtractor
from scrapy.spiders import Spider
from tutorial.items import TutorialItem
from scrapy import Request
from scrapy_splash import SplashRequest

import sys

import re
list = []
#dict = {}
class TaobaoProductsSpider(Spider):
    name = 'mi'
    allowed_domains=['mobile.mi.com', 'm.buy.mi.com']
    #url_pattern = [r'.*rank=sale&type=hot.*']
    #url_extractor = LxmlLinkExtractor(allow=url_pattern)
    #item_dict = {}
    def start_requests(self):
        start_url = ["http://mobile.mi.com/in/category/"]
        splash_args = {
            'wait' : 0.5,
            'html' : 1
        }
        for url in start_url:
            yield  SplashRequest(url, callback = self.parse,
                                args=splash_args)


    def parse(self, response):
        link_list =re.findall(r"(?<=href=\").+?(?=\")", response.body)
        urls = []
        urls1 = []
        urls2 = []
        urlExp1 = 'http://m.buy.mi.com/in/accessories/152'
        urlExp2 = 'http://m.buy.mi.com/in/accessories/213'
        for url in link_list :
                #if url.find("product_id") != -1 :
                    #urls1.append(url)
                if url.find("m.buy.mi.com/in/accessories") != -1 and url != urlExp1 and url != urlExp2:
                    urls2.append(url)

        #for url in urls1:
        #    print url
        #    splash_args = {
        #    'wait' : 0.5,
        #    'html' : 1
        #    }
        #    yield SplashRequest(url, callback = self.parse_next_one,
        #                        args=splash_args)

        for url in urls2:
            print url
            splash_args = {
            'wait' : 0.5,
            'html' : 1
            }
            yield SplashRequest(url, callback = self.parse_next_two,
                                args=splash_args)

    def parse_next_one(self, response):
        name = response.xpath('//div[@class = "add-to-cart"]/div[1]/p[1]/text()').extract()[0].strip()

        if name.find('Lite') != -1 :
            sale = response.xpath('//div[@class = "add-to-cart"]/span/text()').extract()[0].strip()
        else :
            sale = response.xpath('//div[@class = "add-to-cart"]/div[2]/span/text()').extract()[0].strip()
            if sale == [] :
                sale = response.xpath('//div[@class = "add-to-cart"]/div[2]/text()').extract()[0].strip()

        item = TutorialItem()
        item['name'] = name
        item['sale'] = sale
        s = sale.encode('unicode-escape').decode('string_escape')
        print s
        if s == "BUY NOW" :
            item['count'] = 0
        else :
            item['count'] = 1
            #print name
            list.append(name)
        yield item


    def parse_next_two(self, response):
        url = response.url
        link_list = re.findall(r"(?<=href=\").+?(?=\")", response.body)
        urls3 = []
        for url in link_list :
            if url.find("m.buy.mi.com/in/item/3") != -1 :
                urls3.append(url)
        for url in urls3:
            print url
            splash_args = {
            'wait' : 0.5,
            'html' : 1
            }
            yield SplashRequest(url, callback = self.parse_next_again,
                                args=splash_args)

    def parse_next_again(self, response) :
        item = TutorialItem()
        name = response.xpath('//div[@class = "add-to-cart"]/div[1]/p[1]/text()').extract()[0]
        x = response.xpath('//div[@class = "add-to-cart"]/span/text()').extract()
        y = response.xpath('//div[@class = "add-to-cart"]/a/text()').extract()
        if x != [] :
            sale = x
        if y != [] :
            sale = y
        if x == [] and y == [] :
            sale = response.xpath('//div[@class = "add-to-cart"]/div[2]/span/text()').extract()
        #color = response.xpath('//div[]')
        item['name'] = name
        item['sale'] = sale[0].strip()
        s = sale[0].strip().encode('unicode-escape').decode('string_escape')
        print s
        if s == "Notify me" :
            item['count'] = 1
        else :
            item['count'] = 0
            #print name
            list.append(name)
        #print(list)
        yield item

