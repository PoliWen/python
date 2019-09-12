#爬虫demo一，爬取豆瓣top250强电影的名称
import requests as http 
from bs4 import BeautifulSoup
import csv
import os
import re
import mysql.connector
url = 'https://movie.douban.com/top250'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'
}
movie = []
n = 0
def get_movies_top250(url,save_method='csv'):
    '''
    获取一页的数据
    '''
    res = http.get(url,headers = headers)
    soup = BeautifulSoup(res.text,'html.parser')
    moviesDom = soup.select('.item .info')
    for item in moviesDom:
        data = {}
        data['name'] = item.select('.hd .title')[0].string
        #容错代码
        try:
            data['othername'] = item.select('.hd .other')[0].string
        except Exception as e:
            print(e)
            data['othername'] = 'None'
        director_str = item.select('.bd p:nth-of-type(1)')[0].get_text()
        #上映年份
        showtime = director_str.split('\n')[2]
        data['year'] = re.search(r'^.*(\d{4}).*',showtime,re.I|re.M).group(1)
        data['country'] = re.search(r'^.*\d*\s+/\s+(.*)\s+/\s+.*',showtime,re.I|re.M).group(1)
        data['category'] = re.search(r'^.*\d*\s+/\s+.*\s+/\s+(.*)',showtime,re.I|re.M).group(1)
        #print(data['year'],data['country'],data['category'])
        try:
             director_str2 = re.search(r'^.*导演:(.*\s{2,4})主.*...$',director_str,re.I|re.M).group(1) #
        except Exception as e:
             #print('='*30)
             print(e)
             director_str2 = re.search(r'^.*导演:(.*\s{2,4}).*...$',director_str,re.I|re.M).group(1) #
             #print(director_str2)
             #print('codeing is so easy')
        data['director'] = director_str2.strip()
        data['score'] = item.select('.bd .star .rating_num')[0].string
        data['comment_num'] = item.select('.bd .star span')[3].string.replace('人评价','')
        if save_method=='csv':
            save_data_to_csv(data)
        elif save_method == 'mysql':
            save_data_to_mysql(data)

def get_pages_data(save_method='csv'):
    '''
    获取分页的数据
    '''
    if save_method=='csv':
        write_csv_header()  #先清空表里面的数据，写入表头
    for i in range(11):     #循环获取分页的数据
        url = 'https://movie.douban.com/top250?start='+ str(25*(i))
        get_movies_top250(url)
    with open('os/doubanmovie_top250.txt','w',encoding='utf-8') as f:
        f.write('豆瓣电影top250\n') #如何将数据保存到csv文件里面,或者存到数据里面去?
        f.write('\n'.join(movie))
        print('成功写入数据')
        f.close()
    return movie  #返回总数据

def write_csv_header():
    '''
    在追加csv文件之前先清空数据，并且写入头文件
    '''
    filename = os.path.basename(__file__) +".csv"
    with open('os/' + filename, "w", newline="", encoding='utf-8') as f:
        writer = csv.writer(f, dialect="excel")
        writer.writerow(['电影名称','电影别名','电影导演','上映时间','上映国家','分类','评分','评价人数'])
        print('添加表头成功')

def save_data_to_csv(data):
    '''
    将数据保存成一个csv文件
    '''
    global n #函数内部调用函数外部变量必须要在函数内部声明为全局变量
    n += 1
    filename = os.path.basename(__file__) +".csv" #获取当前的文件名
    with open('os/' + filename, "a", newline="", encoding='utf-8') as f:
        writer = csv.writer(f, dialect="excel")
        writer.writerow([data['name'],data['othername'], data['director'],data['year'],
        data['country'],data['category'],data['score'],data['comment_num']])
    print('成功添加'+ str(n) +'条数据')

#连接数据库
def creatdb():
    try:
        mydb = mysql.connector.connect(
            host='localhost',       #数据库主机地址
            user='root',            #数据库用户名
            password='root',        #数据库密码
        )
        #定义数据库的指针
        mycursor = mydb.cursor()
        mycursor.execute("create database doubanmovie")
        print('数据库创造成功')
        print(mycursor)
    except Exception as e:
        print(type(e))
        # if 'database exists' in e:
        #     print('数据库已经存在，请删除数据库之后重新建立数据库')
    
def save_data_to_mysql():
    '''
    将数据保存到mysql里面去
    '''
   
def main():
    print(get_pages_data())
    print(len(movie))

if __name__ == '__main__':
    main()
    creatdb()