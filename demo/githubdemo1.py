#github爬虫,监测关注的库是否有更新，有更新则打开版本库
#https://api.github.com/repos/huge-success/sanic
#web_url https://github.com/huge-success/sanic
import requests as http
import webbrowser
import time
from bs4 import BeautifulSoup

headers = {
    'user-agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'
}
api_url  = 'https://api.github.com/repos/huge-success/sanic'
web_page = 'https://github.com/huge-success/sanic'

last_time = '2019-08-17T09:14:58Z' #上次的时间
def check_update():
    '''
    监测一个版本库的代码是否有更新有更新则打开这个版本库，
    这个函数其实没多大的实际意义
    '''
    global last_time
    rs = http.get(api_url,headers = headers).json()
    cur_time = rs['updated_at']  #最近更新的时间
    while True:
        if not last_time:
            last_time = cur_time
        if last_time < cur_time:
            webbrowser.open(web_page)
        time.sleep(600)
    
def main():
    check_update()

if __name__=='__main__':
    main()