#爬虫demo一，爬取豆瓣top250强电影的名称
import requests as http 
from bs4 import BeautifulSoup
import csv
import os
url = 'https://movie.douban.com/top250'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'
}
movie = []
def get_movies_top250(url,sava_method='csv'):
    '''
    获取一页的数据
    '''
    res = http.get(url,headers = headers)
    soup = BeautifulSoup(res.text,'html.parser')
    moviesDom = soup.select('.item .info')
    for item in moviesDom:
        data = {}
        print('成功获取一条数据')
        data['name'] = item.select('.hd .title:nth-of-type(1)').string
        data['eglishName'] = item.select('.hd .title:nth-of-type(2)').string
        data['eglishName'] = item.select('.hd .title:nth-of-type(2)').string
        data['director'] = item.select('.bd p:nth-of-type(1)').string
        data['score'] = item.select('.bd .star .rating_num').string
        save_data_to_csv(data)
def get_pages_data():
    '''
    获取分页的数据
    '''
    for i in range(11):
        url = 'https://movie.douban.com/top250?start='+ str(25*(i))
        get_movies_top250(url);
    with open('os/doubanmovie_top250.txt','w',encoding='utf-8') as f:
        f.write('豆瓣电影top250\n') #如何将数据保存到csv文件里面,或者存到数据里面去?
        f.write('\n'.join(movie))
        print('成功写入数据')
        f.close()
    return movie  #返回总数据
def save_data_to_csv(data):
    '''
    将数据保存成一个csv文件
    '''
    filename = os.path.basename(__file__) +".csv"
    with open('os/' + filename, "a", newline="", encoding='utf-8') as f:
        writer = csv.writer(f, dialect="excel")
        writer.writerow([data['no'],data['username'], data['usercountry'],
        data['buyer_feedback'], data['star'], data['feedback_time']])

def save_data_to_mysql():
    '''
    将数据保存到mysql里面去
    '''
def main():
    print(get_pages_data())
    print(len(movie))

if __name__ == '__main__':
    main()