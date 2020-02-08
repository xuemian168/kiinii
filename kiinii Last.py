from bs4 import BeautifulSoup
import requests

def Photo():
    def get_html(url):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36',
            'Referer': 'https://kiinii.com/blog/101979/',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Connection': 'keep-alive',
            'Accept-Encoding': 'gzip,deflate,br',
            'Accept-Language': 'zh,en-US;q=0.9,en;q=0.8,zh-CN;q=0.7'
        }
        response = requests.get(url, headers=headers)
        html = response.text
        return html
    n = 0
    art = input('输入文章号:')
    arturl = 'https://kiinii.com/blog/' + art + '/'
    cdn = 'https://sogoke-photo-image.kiinii.com/media/photos/'
    soup = BeautifulSoup(get_html(arturl), 'lxml')
    try:
        title = soup.title.text
        print(title)
    except AttributeError as e:
        return "标签异常"
    for data1 in soup.find_all('div', class_='blog-content sogoke-text-area mb40'):
        for data2 in data1.find_all('img'):
            data1 = data2.get('data-suid')
            downurl = cdn + data1
            print("正在下载",str(n+1))
            n+=1
            try:
                r = requests.get(downurl)
                with open('E:/test/'+(str(n + 1)) + '.jpg', 'wb') as code:
                    code.write(r.content)
                    n += 1
                    print('下载完成')
            except:
                pass
def formatFloat(num):
    return '{:.2f}'.format(num)
def Vedio():
    def get_html(url):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36',
            'Referer': 'https://kiinii.com/blog/101979/',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Connection': 'keep-alive',
            'Accept-Encoding': 'gzip,deflate,br',
            'Accept-Language': 'zh,en-US;q=0.9,en;q=0.8,zh-CN;q=0.7'
        }
        response = requests.get(url, headers=headers)
        html = response.text
        return html
    n = 1
    n += 1
    art = input('输入文章号:')
    path = input('请输入保存路径:(如E:/test/,输入local为脚本所在目录)')
    if path == 'local':
        path = './'
    arturl = 'https://kiinii.com/videoclass/' + art + '/'
    soup = BeautifulSoup(get_html(arturl), 'lxml')
    for data1 in soup.find_all('div', class_='main-video w1000'):
        for data2 in data1.find_all('video'):
            data1 = data2.get('src')
            downurl = data1
            try:
                print('视频正在下载 可能比较慢 路径为：', path)
                r = requests.get(downurl)
                with open(path+(str(n + 1)) + '.mp4', 'wb') as code:
                    code.write(r.content)
                    n += 1
            except:
                print('出现错误 该页面没有找到视频或其他错误')
                pass
def choice():
    which = input('\n输入1启动抓图片 \n输入2启动抓视频\n请输入：')
    if which == '1':
        Photo()
    if which == '2':
        Vedio()
    else:
        print('\n输入有误 重新选择\n输入有误 重新选择\n输入有误 重新选择')
        choice()
choice()