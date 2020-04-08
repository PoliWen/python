#我关注的领域的是否有新的库更新了，并且发送信息给到我的手机
# https://api.github.com/search/repositories?q=django        #
# https://api.github.com/search/repositories?q=topic:django  #相关的主题

import requests as http
import webbrowser
import time
from bs4 import BeautifulSoup


def get_names():
    '''
    输入你要查询的库
    '''
    print('输入你需要查询的库一空格分开')
    names = input()
    return names.split() 

def check_repos(names):
    '''
    查询库的starts数，fork数，生态数
    
    '''
    headers = {
        'user-agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'
    }
    repos_api = 'https://api.github.com/search/repositories?q='
    ecosys_api = 'https://api.github.com/search/repositories?q=topic:'
    for name in names:
        reposinfo = http.get(repos_api+name).json()['items'][0]
        starts = reposinfo['stargazers_count']
        forks = reposinfo['forks_count']
        ecosysinfo = http.get(ecosys_api+name).json()['total_count']
        print(name)
        print('starts:' + str(starts))
        print('forks:' + str(forks))
        print('ecosysinfo:' + str(ecosysinfo))
        print('='*30)
    #多个循环的时候代码会出现问题
def main():
    '''
    查询django,flask,bottle,sanic三个库的使用情况
    '''
    name = get_names()
    print(name)
    check_repos(name)
    #需要翻墙，不然查询好慢呀

if __name__=='__main__':
    main()
    