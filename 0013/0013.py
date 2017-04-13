import urllib.request
import re
import os

def get_img_url(url):
    userAgent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
    headers = {'User-Agent': userAgent}
    request = urllib.request.Request(url, headers=headers)
    response = urllib.request.urlopen(request)
    html = response.read().decode('utf-8')
    pattern = re.compile('(http://imgsrc.baidu.com/forum/.*?)"')
    img_urls = re.findall(pattern, html)
    print(img_urls)
    download_img(img_urls)


def download_img(urls):
    for url in urls:
        data = urllib.request.urlopen(url).read()
        name = re.split('/', url)[-1]
        file = open('img/'+name, 'wb')
        file.write(data)
        file.close()


if __name__ == '__main__':
    if not os.path.exists('img'):  # 创建存放目录
        os.mkdir('img')
    get_img_url('http://tieba.baidu.com/p/2166231880')