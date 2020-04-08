'''
@Author: kingw
@Date: 2020-03-09 18:21:50
@Description: file content
'''
#如何用python连接数据库,9月份开始学习的，从明天起，每天至少写100行，坚持100天
import mysql.connector
mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd = 'root',
    database='python_mysql_learn',
    buffered = True
)
mycursor = mydb.cursor()
#学学学，用用用，忘记了，又重新学，我就不信这个邪了，总是忘记，妈妈比的
#mycursor.execute('create database xxoo')
#mycursor.execute('CREATE TABLE sites2 (name VARCHAR(255), url VARCHAR(255))')
#使用show databases来查看存在那些数据库
#使用show tables来查看数据库里面存在哪些表
mycursor.execute('show tables')
for x in mycursor:
    print('数据库里面有',x)
#往数据库插入一条数据
#往数据库里面新增一条数据
sql = "INSERT INTO sites (name, url) VALUES (%s, %s)"
val = [
  ('Google', 'https://www.google.com'),
  ('Github', 'https://www.github.com'),
  ('Taobao', 'https://www.taobao.com'),
  ('stackoverflow', 'https://www.stackoverflow.com/')
]
#使用executemany()方法进行批量插入
mycursor.executemany(sql, val)
mydb.commit()  #数据库有更新就要执行这条代码

#查找数据
mycursor.execute('select * from sites order by name')
print(mycursor.rowcount,'批量插入数据')
#查找所有的数据
#fetchall获取所有的数据
myresult = mycursor.fetchall()
#查找一条数据使用fetchone()
i=0
for x in myresult:
    print(x)
    i=i+1
    print(f'获取{i}条数据成功')

#按条件查找
sql = "select * from sites where name='Github'"
mycursor.execute(sql)
result = mycursor.fetchone()
print('ggg',result)
#like条件

#删除一条数据
sql = "DELETE FROM sites WHERE name = 'stackoverflow'"
mycursor.execute(sql)
mydb.commit()
print(mycursor.rowcount,'删除一条数据成功')

#更新一条数据
sql = "UPDATE sites SET name = 'ZH' WHERE name = 'Zhihu'"
mycursor.execute(sql)
mydb.commit()
print(mycursor.rowcount,'更新数据成功')
