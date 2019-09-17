#学习selenium浏览器自动加载功能爬取衡阳安居客的数据
import requests as http 
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
import csv
import os
import re
import mysql.connector
url = 'https://hy.fang.anjuke.com/loupan/all/p1/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'
}
n = 0
def hy_fangjia():
    write_csv_header()
    for i in range(1):
        url = 'https://hy.fang.anjuke.com/loupan/all/p' + str(i) + '/'
        get_data(url)

def get_data(url):
    #自动化测试，自己写脚本记性自动化点击
    res = http.get(url,headers = headers)
    soup = BeautifulSoup(res.text,'html.parser')
    fj_dom = soup.select('.item-mod')
    with open('os/hyfj.html','w',encoding='utf-8') as f:
        f.write(soup.prettify())
        f.close()
    print(fj_dom)
    for each_item in fj_dom:
        data = {}
        print('.'*30)
        data['house_name'] = each_item.select('.items-name')[0].string
        data['house_address'] = each_item.select('.list-map')[0].string
        data['house_area'] = each_item.select('.huxing')[0].string
        data['house_price'] = each_item.select('.price')[0].string
        data['house_tag'] = each_item.select('.tag-panel')[0].string
        save_data_to_csv(data)

def write_csv_header():
    '''
    在追加csv文件之前先清空数据，并且写入头文件
    '''
    filename = os.path.basename(__file__) +".csv"
    with open('os/' + filename, "w", newline="", encoding='utf-8') as f:
        writer = csv.writer(f, dialect="excel")
        writer.writerow(['楼盘名称','楼盘地址','户型与面积','价格','标签'])
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
        writer.writerow([data['house_name'],data['house_address'], data['house_area'],data['house_price'],
        data['house_tag']])
    print('成功添加'+ str(n) +'条数据')

#找一个项目实战
def main():
    hy_fangjia()

if __name__ == '__main__':
    main()
