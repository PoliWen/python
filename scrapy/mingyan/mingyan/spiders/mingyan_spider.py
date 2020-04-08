# -*- coding: utf-8 -*-
import scrapy
class mingyan_Spider(scrapy.Spider):
    name = 'mingyanspider'
    start_urls=[
            'http://lab.scrapyd.cn/page/1/',
            'http://lab.scrapyd.cn/page/2/',
    ]
    def parse(self, response):
        page = response.url.split('/')[-2]
        filename = 'mingyan_%s.html'%page
        print('='*30)
        print(filename)
        with open(filename,'wb') as f:
            f.write(response.body)
            f.close()
        print('打印日志%s'%filename)
