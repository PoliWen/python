#学习selenium浏览器自动加载功能
import requests as http 
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
import csv
import os
import re
import mysql.connector
url = 'https://movie.douban.com/top250'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'
}
def loginTomtop():
    caps = webdriver.DesiredCapabilities().FIREFOX
    caps['marionette'] = False
    binary = FirefoxBinary(r"C:\Program Files (x86)\Mozilla Firefox\firefox.exe")
    #firefox有问题应该是工具跟浏览的版本对不上，后续有那空继续研究，
    #chrome浏览器也报错的问题解答文章：https://blog.csdn.net/qq_26200629/article/details/86141131
    chorme_driver = r'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe'
    browser= webdriver.Chrome(executable_path = chorme_driver)  #用火狐浏览器打开
    browser.get(url)
    #自动化测试，自己写脚本记性自动化点击
    user = browser.find_element_by_name('email')
    pwd = browser.find_element_by_name('pw')
    user.send_keys('2851823532@qq.com')
    pwd.send_keys('123456')
    browser.find_element_by_css_selector('.signIn_btn').click()

#找一个项目实战
def main():
    loginTomtop()

if __name__ == '__main__':
    main()
