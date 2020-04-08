# -*- coding: utf-8 -*-
import scrapy
class mingyan_Spider(scrapy.Spider):
    name = 'mingyanspider2'
    start_urls=['http://lab.scrapyd.cn/page/'+ str(x) +'/' for x in range(7)]
    
    def parse(self, response):
        '''
        转换代码
        '''
        mingyan = response.css('div.quote')
        data = []
        for item in mingyan:
            text = item.css('.text::text').extract_first()
            author = item.css('.author::text').extract_first()
            tag = item.css('.tags .tag::text').extract()
            tags = ','.join(tag)
            data.append('内容:'+text+'\t作者:'+ author +'\t标签:' + tags)
            print('添加一条数据成功')
        with open('mingyanspider2.txt','a+') as f:
            f.write('\n'.join(data))
            f.close()
    #用scrapy爬虫跟不用scrapy爬虫有什么区别。

