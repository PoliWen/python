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

#连接数据库,这样就要用全局class了
class mysql_class():
    '''
    构建一个链接数据库的class
    '''
    def __init__(self,tableName,databaseConfig):
        self.conn = mysql.connector.connect(**databaseConfig)
        self.cursor = self.conn.cursor()
        self.tableName = tableName
    def createtable(self):
        try:
            mycursor = self.cursor
            mycursor.execute("show TABLES")  #取出数据库里面的所有数据表
            datatable_exists = False  #判断个数据表是否存在这么麻烦
            for x in mycursor:
                print(x[0])
                print(type(x[0]))
                if str(x[0]) == self.tableName: #注意创建的数据表取出来的名字都是小写
                    datatable_exists = True
            print(datatable_exists)
            create_table_sql = f'''
            create table {self.tableName}(
                movies_id int auto_increment not null,
                movies_name varchar(100) not  null,
                movies_alias varchar(100) not null,
                movies_director varchar(100) not null,
                release_time varchar(100) not null,
                release_country varchar(100) not null,
                movies_category varchar(100) not null,
                movies_score varchar(10) not null,
                evalute integer not null,
                primary key (movies_id)
            );
            '''
            if datatable_exists:
                mycursor.execute(f"drop table {self.tableName}")
                mycursor.execute(create_table_sql)
                print('删除旧的数据表，创建新的数据表成功。')
            else:
                mycursor.execute(create_table_sql)
                print('创建数据表成功。')
        except Exception as e:
            print(type(e))

    def save_data_to_mysql(self,data):
        sql = f'''insert into doubanmovietop250 (movies_name,movies_alias,movies_director,release_time,release_country,movies_category,movies_score,evalute) values ('{data[0]}','{data[1]}','{data[2]}','{data[3]}','{data[4]}','{data[5]}','{data[6]}','{data[7]}');'''
        print(sql)
        print(data)
        self.cursor.execute(sql)
        self.conn.commit()
        print('成功插入一条数据')

movie = []
n = 0
def get_movies_top250(url,mydb,save_method):
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
            data['othername'] = item.select('.hd .other')[0].string.replace('/','').strip().replace("'","\\'") #插入到mysql的特殊字符必须要进行先转义，不然插入的sql语句会报错
            print('*'*30)
            print(data['othername'])
        except Exception as e:
            print(e)
            data['othername'] = 'None'
        director_str = item.select('.bd p:nth-of-type(1)')[0].get_text()
        #上映年份
        showtime = director_str.split('\n')[2]
        #print(data['year'],data['country'],data['category'])
        try:
             director_str2 = re.search(r'^.*导演:(.*\s{2,4})主.*...$',director_str,re.I|re.M).group(1) #
        except Exception as e:
             #print('='*30)z
             print(e)
             director_str2 = re.search(r'^.*导演:(.*\s{2,4}).*...$',director_str,re.I|re.M).group(1) #
             #print(director_str2)
             #print('codeing is so easy')
        data['director'] = director_str2.strip()
        data['year'] = re.search(r'^.*(\d{4}).*',showtime,re.I|re.M).group(1)
        data['country'] = re.search(r'^.*\d*\s+/\s+(.*)\s+/\s+.*',showtime,re.I|re.M).group(1)
        data['category'] = re.search(r'^.*\d*\s+/\s+.*\s+/\s+(.*)',showtime,re.I|re.M).group(1)
        data['score'] = item.select('.bd .star .rating_num')[0].string
        data['comment_num'] = item.select('.bd .star span')[3].string.replace('人评价','')
        if save_method=='csv':
            save_data_to_csv(data)
        elif save_method == 'mysql':
            dataList = []
            for x, y in data.items():
                dataList.append(y)
            print(tuple(dataList))
            # 往数据库里面添加数据
            mydb.save_data_to_mysql(tuple(dataList))

def get_pages_data(save_method='csv'):
    '''
    获取分页的数据
    '''
    save_method = save_method
    if save_method == 'csv':
        write_csv_header()  #先清空表里面的数据，写入表头
        for i in range(11):     #循环获取分页的数据
            url = 'https://movie.douban.com/top250?start='+ str(25*(i))
            mydb = 'csv'
            get_movies_top250(url,mydb,save_method)
    else:
        #简单的创建一个数据库
        databaseConfig = {
            'host':'localhost',       #数据库主机地址
            'user':'root',            #数据库用户名
            'password':'root',        #数据库密码
            'database':'doubanmovie'  #豆瓣电影
        }
        #实例化数连接数据库
        mydb = mysql_class('doubanmovietop250',databaseConfig)
        mydb.createtable()
        for i in range(11): #循环获取分页的数据
            url = 'https://movie.douban.com/top250?start='+ str(25*(i))
            get_movies_top250(url,mydb,save_method)
    
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

def main():
    print(get_pages_data(save_method='mysql'))

if __name__ == '__main__':
    main()
