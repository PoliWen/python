# requests高级用法
# 需要好好研究python的魔术方法

import requests as http
BASE_URL = 'https://api.github.com'

def build_url(end_point):
    '''
    处理url
    '''
    return '/'.join([BASE_URL,end_point])

def basic_auth():
    '''
    基础验证,需要进行登录认证
    '''
    response = http.get(build_url('user'),auth=('873619879@qq.com','wyh13046346113./>'))
    print(response.text)
    print(response.request.headers)

#用token验证不会暴露用户隐私，更安全 =
def basic_oauth():
    headers = {
        'Authorization':'token 107c5da093401bbbb8cfdf0d8a1aef57bbe0bc9c'
    }
    response = http.get(build_url('user/emails'),headers = headers)
    print(response.text)
    print(response.request.headers)
    print(response.status_code)

   
def main():
    #basic_auth()
    basic_oauth()

if __name__=='__main__':
    main()
