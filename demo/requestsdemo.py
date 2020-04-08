'''
@Author: kingw
@Date: 2020-03-11 09:39:55
@Description: file content
'''
#python中 requests库的使用
#查看这篇文章：https://www.cnblogs.com/TMesh/p/11862986.html
import requests as http
import json
res = http.get('https://www.tomtop.com')
print(res.text)
print(res.content)
#这样就把一个html页面下载下来了，python很牛逼呀，可以做很多事情呀
#注意写入的时候不能创建文件夹，只能创建文件，如果文件夹不存在则会报错
fs = open('file/index.html','w',encoding='utf-8')
fs.write(res.text)
fs.close()
request = http.get('http://httpbin.org/get')
print(request.text)
print(type(request.text))
#json.loads()是把拿到的json字符串转化为python可以用的字典数据，json.dumps()是把字典数据转化为json字符串
print(type(json.loads(request.text)))
print(json.loads(request.text))
#有些网址必须要传入headers
headers = {
'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
}
zhihu = http.get('https://www.zhihu.com',headers=headers)
with open('file/zhihu.html','w',encoding='utf-8') as f:
    f.write(zhihu.text)
    print('写入知乎的数据成功')
    f.close()
#使用post传递数据
data = {
    'name':'wxl',
    'age':'30'
}
response = http.post('http://httpbin.org/post',data=data)
print(response.text)
print('这么简单的东西，看一篇文章就解决了，你居然要看这么久，你的性格太稳定了，太稳定会让你错失太多的机会')
print(type(response.status_code), response.status_code)
print(type(response.headers), response.headers)
print(type(response.cookies), response.cookies)
print(type(response.url), response.url)
print(type(response.history), response.history)


