# author:薛建国
# update date:2018-02-12
# 速卖通评论抓取爬虫
# 基于多线程以及线程安全队列
# 使用代理
from requests.adapters import HTTPAdapter
from bs4 import BeautifulSoup
import mysql.connector
import os, time,random
import threading
import requests
import queue
import csv
import sys
# 获取评论总页数
def get_total_page(url):
    total_page=0
    headers={
        'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',        
    }
    try:
        res=requests.get(url,headers=headers,timeout=30)
        soup=BeautifulSoup(res.text,'html.parser')
        tpage=int(soup.select('#simple-pager')[0].select('.ui-label')[0].text.split('/')[1])
        total_page=tpage
        # 速卖通平台评论500页之后，均返回第一页数据
        if total_page>=500:
            total_page=500
            print('总共有' + str(total_page) + '页')
    except requests.RequestException as e:
        print("requestsException")
        print(e)
    except requests.ConnectionError as e:
        print("connectionError")
        print(e)
    except requests.HTTPError as e:
        print("httpError")
        print(e)
    except requests.URLRequired as e:
        print('urlRequired')
        print(e)
    except requests.ConnectTimeout as e:
        print("connectTimeout")
        print(e)
    except requests.ReadTimeout as e:
        print("readTimeout")
        print(e)
    except Exception as e:
        print("获取总页数失败")
        print("失败信息")
        print(e)
    finally:
        return total_page
# 用于根据productid，ownerid,companyid构造获取token url
def get_url(productid,owner_memberid,companyid,member_type="seller",start_valid_date="",il8n="true"):
    host="https://feedback.aliexpress.com/display/productEvaluation.htm?v=2&"
    url=host+"productId="+productid
    url+="&ownerMemberId="+owner_memberid
    url+="&companyId="+companyid
    url+="&memberType="+member_type
    url+="&startValidDate="+start_valid_date
    url+="s&il8n="+il8n
    return url
# 用于更新iplist.txt文件,需要的时候手动调用
def update_ip_list():
    url='http://www.xicidaili.com/nn/'
    headers={
        'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',        
    }
    web_data=requests.get(url,headers=headers)
    soup=BeautifulSoup(web_data.text,'html.parser')
    ips=soup.select('tr')
    ip_list=[]
    for i in range(1,len(ips)):
        ip_info=ips[i]
        tds=ip_info.select('td')
        ip_list.append(tds[1].text +':'+ tds[2].text)
    with open("os/iplist.txt","a",encoding='utf-8') as f:
            for ip in ip_list:
                f.write(ip)
                f.write('\n')
    return ip_list
class CommentSpyder(threading.Thread):
    headers = {
        'authority': 'feedback.aliexpress.com',
        'method': 'POST',
        'path': '/display/productEvaluation.htm',
        'scheme': 'https',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'zh-CN,zh;q=0.9',
        'cache-control': 'max-age=0',
        'content-length': '337',
        'content-type': 'application/x-www-form-urlencoded',
        'cookie': 'ali_apache_id=11.227.32.216.1564542947520.200687.8; cna=3h2vFZAju0gCAXF0f/NoeQdM; _m_h5_tk=f1f4315eb29131fc645a6884aa56cc15_1564718452309; _m_h5_tk_enc=d2ec41dd1564dc1e60ae62856e070284; ali_apache_track=; ali_apache_tracktmp=; _ga=GA1.2.402536737.1564708014; _gid=GA1.2.1129892137.1564708014; xman_us_f=x_locale=es_ES&x_l=1; intl_locale=es_ES; aep_usuc_f=site=esp&c_tp=USD&region=CN&b_locale=es_ES; acs_usuc_t=acs_rt=ae487af7c3924c6eae921613d1bc1b38&x_csrf=1686dndozbxh6; xman_t=43rmQFPU/SRFqiIDaVQmyuZ7oirjzq1JvnozcFYM7r9QIESWCBm1eyYWiZ9L993NtS8/1Aei4esX4CZGO9IBDjRzDZUFRzJWpVC5nzm4w8M=; xman_f=QiF8vMTK0ivm53TeeapI/uWMbR11oSssbszRBof2X/h2VncR68/aIw3WCfJlOsiqZhejS4xSknE5mvcDiz9ZJH0wb1H1/BddmRYbAQH+eLCXTaTXfSr7MQ==; aep_history=keywords%5E%0Akeywords%09%0A%0Aproduct_selloffer%5E%0Aproduct_selloffer%0932847472228%0932872436973%0932868296257%0932979289526%0932838577721%0932977685024%0932977685024; intl_common_forever=0V4nOygRMfxnvrJ8En+0ko29G73s7BTq/n6S13kSoctAEoDpMrKYTQ==; JSESSIONID=07817A5740E5EE6A1AE0B2EE6BE788D5; isg=BKSkE7SppVTj09EY4gS-J_OpYKJWlcTuC2tLbL7FMG8yaUQz5k2YN9rLKYFUqgD_; l=cBa84ySgqYCzRi_LBOCanurza77OSLAYYuPzaNbMi_5Cw6T63pbOkSXZtF96VjWdtETB4eLrWGp9-etkZrlOCn37w2mC.',
        'origin': 'https://feedback.aliexpress.com',
        'referer': 'https://feedback.aliexpress.com/display/productEvaluation.htm?v=2&productId=32977685024&ownerMemberId=229788063&companyId=239288868&memberType=seller&startValidDate=&i18n=true',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3704.400 QQBrowser/10.4.3587.400'
    }

    # 初始化    
    def __init__(self,url,productid,owner_memberid,companyid,result_queue,start_page=1,end_page=1):
        super().__init__()
        self.url=url
        self.posturl="https://feedback.aliexpress.com/display/productEvaluation.htm"      
        self.productid=productid
        self.owner_memberid=owner_memberid
        self.companyid=companyid
        self.result_queue = result_queue
        self.start_page=start_page
        self.end_page=end_page
        if(self.productid=='' or self.owner_memberid=='' or self.companyid==''):
            print('初始化失败')
            print('请输入产品编号，店主编号，以及公司编号')
            return
        self.session=requests.Session()
        self.session.keep_live=False
        self.ip_list=self.get_ip_list()       
        self.data=dict()
        self.create_post_data()
        print("报告老大:知客爬虫初始化已完毕,等待爬取数据")
    # 构造post data对象
    def create_post_data(self):
        self.data['ownerMemberId']=self.owner_memberid
        self.data['memberType']='seller'
        self.data['productId']=self.productid
        self.data['companyId']=''
        self.data['evaStarFilterValue']='all Stars'
        self.data['evaSortValue']='sortdefault@feedback'
        self.data['startValidDate']=''
        self.data['i18n']='true'
        self.data['withPictures']='false'
        self.data['withPersonalInfo']='false'
        self.data['withAdditionalFeedback']='false'
        self.data['onlyFromMyCountry']='false'
        self.data['isOpened']='true'
        self.data['version']='evaNlpV1_2'
        self.data['translate']='Y'
        self.data['jumpToTop']='false'
        self.data['v']='2'
    # 读取iplist为一个list
    def get_ip_list(self):
        temp_ip_list=[]
        with open('os/iplist.txt', 'r') as f:
            while True:
                ip=f.readline().replace('\n','')
                temp_ip_list.append('http://'+ip)
                if not ip:
                    break
        return temp_ip_list
    # 从self.iplist中随机选择一个ip     
    def get_random_ip(self):    
        proxy_ip= random.choice(self.ip_list)
        proxies = {
            'http':proxy_ip
        }
        return proxies
    # 评论页面解析函数，参数为html页面
    def parse_comment(self,comment_html):
        try:
            comment_soup=BeautifulSoup(comment_html.text,'html.parser')
        except Exception as e:
            print("suop构造失败")
            print(e)
            return 
        try:               
            feedback_star=comment_soup.select('.star-view')
            fb_mains=comment_soup.select('.fb-main')
            user_info=comment_soup.select('.fb-user-info')
            for i in range(0,len(fb_mains)):
                temp=[]
                try:
                    username=user_info[i].select('.user-name')[0].text.replace('\t','').replace('\n','')
                except Exception as e:
                    username=''
                try:
                    usercountry=user_info[i].select('.user-country')[0].text.replace('\t','').replace('\n','')
                except:
                    usercountry=''
                try:
                    star=int(fb_mains[i].select('.star-view')[0].select('span')[0]['style'].lstrip('width:').rstrip('%'))/20
                except Exception as e:
                    star=0
                try:
                    buyer_review=fb_mains[i].select('.buyer-review')[0]
                    buyer_feedback=buyer_review.select('.buyer-feedback')[0].select('span')[0].text.lstrip(' ').rstrip(' ').replace('\t',' ').replace('\n',' ')
                except Exception as e:
                    buyer_feedback=''
                try:
                    feedback_time=buyer_review.select('.r-time')[0].text
                except Exception as e:
                    feedback_time=''
                try:
                    additional_review=fb_mains[i].select('.buyer-addition-feedback')
                    if len(additional_review)>0:
                        additional_feedback=additional_review[0].text.lstrip(' ').rstrip(' ').replace('\t',' ').replace('\n',' ')
                    else:
                        additional_feedback=''
                except Exception as e:
                    additional_feedback=''
                    print(e)
                tempData=dict()
                tempData['username']=username
                tempData['usercountry']=usercountry
                tempData['buyer_feedback']=buyer_feedback
                tempData['star']=star
                tempData['feedback_time']=feedback_time
                tempData['additional_feedback']=additional_feedback
                print(tempData)
                print('ooooooooooooooooooooooooooooooooooooooooo')
                print('\n')
                self.result_queue.put(tempData)
        except Exception as e:
            print("解析出错")
            print("出错信息")
            print(e)
    # 按页爬取评论，参数为page
    def crawl_comment_by_page(self,page):
        current_page=page-1
        if current_page==0:
            current_page=2
        self.data['page']= str(page)
        self.data['currentPage'] = str(current_page)
        try:
            proxies=self.get_random_ip()
            comment_html=self.session.post(self.posturl,headers=self.headers,data=self.data,timeout=30,proxies=proxies)            
            self.parse_comment(comment_html)
        except requests.RequestException as e:
            print("requestsException")
            print(e)
        except requests.ConnectionError as e:
            print("connectionError")
            print(e)
        except requests.HTTPError as e:
            print("httpError")
            print(e)
        except requests.URLRequired as e:
            print('urlRequired')
            print(e)
        except requests.ConnectTimeout as e:
            print("connectTimeout")
            print(e)
        except requests.ReadTimeout as e:
            print("readTimeout")
            print(e)
        except Exception as e:
            print("爬取出错")
            print("出错信息")
            print(e)
    def run(self):
        start=self.start_page
        end=self.end_page
        while start <=end:
            self.crawl_comment_by_page(start)          
            start=start+1
            time.sleep(3)
# saver线程，用于从队列中取数据,并保存
class Saver(threading.Thread):
    def __init__(self,result_queue,productid,owner_memberid,method='csv',db='aliexpress',user='root',password='root'):
        super().__init__()
        self.result_queue = result_queue
        self.productid=productid
        self.owner_memberid=owner_memberid        
        self.method = method
        self.db=db
        self.user=user
        self.password=password
        self.conn= mysql.connector.connect(user=self.user, password=self.password,database=self.db)
    def save_data_to_csv(self,data):
        filename = self.owner_memberid + self.productid+".csv"
        with open('os/'+ filename,"a",newline = "",encoding='utf-8') as f:
            writer = csv.writer(f,dialect = "excel")
            writer.writerow([data['no'],self.productid,data['username'],data['usercountry'],data['buyer_feedback'],data['star'],data['feedback_time'],data['additional_feedback']])
    def save_data_to_db(self,data):
        try:
            cursor = self.conn.cursor()
            cursor.execute('insert into comment (no,productid,username,usercountry,buyer_feedback,star,feedback_time,additional_feedback) values (%s,%s,%s,%s,%s,%s,%s,%s)',[data['no'],self.productid,data['username'],data['usercountry'],data['buyer_feedback'],data['star'],data['feedback_time'],data['additional_feedback']])
            self.conn.commit()
        except Exception as e:
            print("插入数据出错")
            print(e)      
    def run(self):
        i=0
        while True:
            data = self.result_queue.get()
            data['no']=i
            if self.method=='db':
                self.save_data_to_db(data)
            elif self.method=='csv':
                print('==============')
                self.save_data_to_csv(data)
            else:
                pass
            print("插入第"+ str(i) +'条数据')
            i=i+1
    def closeConn(self):
        self.conn.close()
def main(productid,owner_memberid,companyid,thread_num=10):
    result_queue = queue.Queue()
    url= get_url(productid,owner_memberid,companyid)
    print("token Url:"+url)
    # 获取评论总页数
    t1=time.time()
    total_page=get_total_page(url)
    t2=time.time()
    print('获取总页数耗时:' + str(t2-t1))
    spyders=[]
    #根据评论总页数和线程数(默认10)为每个线程平均分配每个线程负责的页码数
    if total_page>0:
        page_num_per_thread=int(total_page/thread_num)   
        for i in range(thread_num):
            print('xxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
            start_page=i*page_num_per_thread+1
            end_page=(i+1)*page_num_per_thread
            if(i==(thread_num-1)):
                end_page=total_page        
            spyder = CommentSpyder(url,productid,owner_memberid,companyid,result_queue,start_page,end_page)
            spyders.append(spyder)
        for spyder in spyders:
            spyder.start()
        saver = Saver(result_queue,productid,owner_memberid)
        saver.daemon = True
        saver.start()
        for i in range(10):
            spyders[i].join()
        saver.closeConn()
if __name__ == '__main__':
    productid="32977685024"
    owner_memberid="229788063"
    companyid="239288868"
    update_ip_list()
    main(productid,owner_memberid,companyid)
    #可以把数据爬下来，但是数据很乱呢
