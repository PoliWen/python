# -*- coding: utf-8 -*-
#利用递归爬取下一页的数据，带参数的爬虫
import scrapy

class argspider(scrapy.Spider):
    name = 'argspider'
    def start_requests(self):
        base_url = 'http://lab.scrapyd.cn/'
        tagname = getattr(self,'tag',None)
        if tagname is not None:
            url = base_url +'tag/' + tagname
        print(url)
        yield scrapy.Request( url = url,callback=self.parse)
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
            print(text,author,tags)
            print('='*30)
            data.append('内容:'+ text +'\t作者:'+ str(author) +'\t标签:' + tags)
            print('添加一条数据成功')
        with open('mingyanspiderags.txt','a+') as f:
            f.write('\n'.join(data))
            f.close()
        next_page = response.css('li.next a::attr(href)').extract_first()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            #使用回调函数，这个yield还是有点不理解，要好好的理解理解了，js里面也有这个概念
            yield scrapy.Request(url = next_page,callback = self.parse)
    #用scrapy爬虫跟不用scrapy爬虫有什么区别。
