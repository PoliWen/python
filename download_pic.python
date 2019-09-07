#用python下载保存一个图片
#继续深入研究这个代码用这个代码下载别人网站上的图片给自己使用
import requests as http

def download_pictrue():
    '''
    下载一个图片并且保存
    '''
    url = 'https://www.imooc.com/static/img/index/logo.png'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3730.400 QQBrowser/10.5.3805.400'
    }
    from contextlib import closing
    with closing(http.get(url,headers = headers,stream = True)) as response:
        with open('os/demo.png','wb') as f:
            #没128字节写入一次
            for chunks in response.iter_content(128):
                f.write(chunks)
            f.close()
def main():
    download_pictrue()
if __name__ =='__main__':
    main()



