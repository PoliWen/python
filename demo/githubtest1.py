'''
@Author: kingw
@Date: 2020-03-24 14:50:26
@Description: file content
'''
#写一个比较github里面库的使用情况，从start数量，fork数量，和生态数量三个维度来进行比较，并且输出他们的结果
import requests as http

def get_name():
    name = input('请输入你要比较的库，使用空格隔开')
    return name.split()
def compare_diff(name):
    for n in name:
        repos_api = 'https://api.github.com/search/repositories?q='
        ecosys_api = 'https://api.github.com/search/repositories?q=topic:'
        res = http.get(repos_api+n).json()
        res2 = http.get(ecosys_api+n).json()
        start_count = res['items'][0]['stargazers_count']
        fork_count = res['items'][0]['forks_count']
        ecosys_count = res2['total_count']
        #vue react jquery
        print(n+'的参数')
        print('start: '+str(start_count))
        print('fork: '+str(fork_count))
        print('ecosys: '+str(ecosys_count))
        print('='*30)
def main():
    name = get_name()
    compare_diff(name)

if __name__=="__main__":
    main()