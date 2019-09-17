#github爬虫,试着用所学知识去发现 Kenneth 今天 Starred 了哪些库，并且自动在浏览器中打开这些库的地址。
#https://api.github.com/users/kennethreitz/starred
#web_url https://github.com/huge-success/sanic
import requests as http
import webbrowser
import time
from bs4 import BeautifulSoup

headers = {
    'user-agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'
}
api_url  = 'https://api.github.com/users/kennethreitz/starred'
web_page = 'https://github.com/huge-success/sanic'

starred = [40684033,152794206,32555448,110339095,162761045,95903923,149144377,47099511,36897953,30933195,132507058,43768227,57192704] #上次的时间
def check_update():
    '''
    监测一个版本库的代码是否有更新有更新则打开这个版本库，
    这个函数其实没多大的实际意义
    '''
    global starred
    # rs = http.get(api_url,headers = headers).json()
    # for i in rs:
    #     starred.append(i['id'])
    while True:
        res = http.get(api_url,headers = headers).json()
        for i in res:
            if not i['id'] in starred:
                starred.append(i['id'])
                repo_name = i['name']
                owner = i['owner']['login']
                web_page = 'https://github.com/'+owner+'/'+repo_name
                webbrowser.open(web_page)
        time.sleep(600)
    
def main():
    check_update()

if __name__=='__main__':
    main()