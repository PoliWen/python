#爬虫爬取速卖通评论数据 import csv
import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt

headers = { #ajax请求就需要写headers请求头信息
	'authority': 'feedback.aliexpress.com',
	'method': 'GET',
	'path': '/display/productEvaluation.htm?v=2&productId=32977685024&ownerMemberId=229788063&companyId=239288868&memberType=seller&startValidDate=&i18n=true',
	'scheme': 'https',
	'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
	'accept-encoding': 'gzip, deflate, br',
	'accept-language': 'zh-CN,zh;q=0.9',
	'cache-control': 'max-age=0',
	'cookie': 'ali_apache_id=11.227.32.216.1564542947520.200687.8; cna=3h2vFZAju0gCAXF0f/NoeQdM; _m_h5_tk=f1f4315eb29131fc645a6884aa56cc15_1564718452309; _m_h5_tk_enc=d2ec41dd1564dc1e60ae62856e070284; ali_apache_track=; ali_apache_tracktmp=; _ga=GA1.2.402536737.1564708014; _gid=GA1.2.1129892137.1564708014; xman_us_f=x_locale=es_ES&x_l=1; intl_locale=es_ES; aep_usuc_f=site=esp&c_tp=USD&region=CN&b_locale=es_ES; acs_usuc_t=acs_rt=ae487af7c3924c6eae921613d1bc1b38&x_csrf=1686dndozbxh6; xman_t=43rmQFPU/SRFqiIDaVQmyuZ7oirjzq1JvnozcFYM7r9QIESWCBm1eyYWiZ9L993NtS8/1Aei4esX4CZGO9IBDjRzDZUFRzJWpVC5nzm4w8M=; xman_f=QiF8vMTK0ivm53TeeapI/uWMbR11oSssbszRBof2X/h2VncR68/aIw3WCfJlOsiqZhejS4xSknE5mvcDiz9ZJH0wb1H1/BddmRYbAQH+eLCXTaTXfSr7MQ==; aep_history=keywords%5E%0Akeywords%09%0A%0Aproduct_selloffer%5E%0Aproduct_selloffer%0932847472228%0932872436973%0932868296257%0932979289526%0932838577721%0932977685024%0932977685024; intl_common_forever=0V4nOygRMfxnvrJ8En+0ko29G73s7BTq/n6S13kSoctAEoDpMrKYTQ==; JSESSIONID=78B4F7C7A261717C8351426671BD3D9F; isg=BN_f4llM_tWn8PrJ7e01RtTAezOp7D-vzJIgXXEsew7VAP-CeRTDNl3SwtDbgwte; l=cBa84ySgqYCzRI3yBOCanurza77OSLAYYuPzaNbMi_5CQ6T6-QbOkSv1PF96VjWdtD8B4eLrWGp9-etkq3cmXnu7w2mC.',
	'upgrade-insecure-requests': '1',
	'user-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3704.400 QQBrowser/10.4.3587.400'
}
url = 'https://feedback.aliexpress.com/display/productEvaluation.htm?v=2&productId=32977685024&ownerMemberId=229788063&companyId=239288868&memberType=seller&startValidDate=&i18n=true'
url2 = 'https://www.tomtop.com/index.php?r=details/default/ajaxreview&spu=L0686&page=2&_=1564709796454'
res = requests.get(url,headers = headers)  #爬虫爬取速卖通的数据，使用你的技术实现变现，只会做前端没一点卵用
print(res)
soup = BeautifulSoup(res.text,'html.parser')
print('===============================')
soup = soup.select('.buyer-review span')
print(type(soup))
stt = ''
fo = open("os/foo.html", "w", encoding='utf-8') #指定encoding是为了解决编码报错
for html in soup:
	stt = stt + str(html)
print(type(stt))
fo.write(stt)
fo.close()
print('===============================')
#到这一步，已经可以拿到数据了，剩下的就是这么处理数据了,
#
import numpy as np
import matplotlib.pyplot as plt
 
mu, sigma = 100, 15
x = mu + sigma * np.random.randn(10000)
 

# 用于更新iplist.txt文件,需要的时候手动调用
def update_ip_list():
    url='http://www.xicidaili.com/nn/'
    headers={
        'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',        
    }
    web_data = requests.get(url,headers=headers)
    soup = BeautifulSoup(web_data.text,'html.parser')
    ips = soup.select('tr')
    ip_list = []
    for i in range(1,len(ips)):
        ip_info = ips[i]
        tds = ip_info.select('td')
        ip_list.append(tds[1].text +':'+ tds[2].text)
    with open("os/iplist.txt","a",encoding='utf-8') as f:
            for ip in ip_list:
                f.write(ip)
                f.write('\n')
    return ip_list

# 直方图
 
n, bins, patches = plt.hist(x, 50, normed=1, facecolor='g', alpha=0.75)
 
 
plt.xlabel('Smarts')
plt.ylabel('Probability')
plt.title('Histogram of IQ')
plt.text(60, .025, r'$\mu=100,\ \sigma=15$')
plt.axis([40, 160, 0, 0.03])
plt.grid(True)
plt.show()


update_ip_list()







