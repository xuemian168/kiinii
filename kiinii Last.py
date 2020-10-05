# -*- coding:utf-8 -*- 
#Time: 2020/10/05/21:22
#Author: JohnserfSeed
#Origin： XueMian
#GitHub: https://github.com/Johnserf-Seed;https://github.com/xuemian168

from lxml import etree
import requests

class kiinii:

    #文件下标
    index = 1

    #资源地址
    blog_url = 'https://kiinii.com/blog/'
    video_url = 'https://www.kiinii.com/videoclass/'

    #UA字典
    headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36',
            'Host': 'kiinii.com',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Connection': 'keep-alive',
            'Accept-Encoding': 'gzip,deflate,br',
            'Accept-Language': 'zh,en-US;q=0.9,en;q=0.8,zh-CN;q=0.7'
        }

    def __init__(self,sid):
        self.down_img(rid)

    #图片下载
    def down_img(self,rid):
        try:
            r = requests.get(self.blog_url + str(rid),headers=self.headers)
            res = etree.HTML(r.text)
            img_url=res.xpath('//img[@class="uploaded_photo"]/@src')
            if(img_url==[]):
                self.down_mp4(rid)
        except:
            #print("此资源为视频资源")
            pass
        else:
            for img in img_url:
                try:
                    print("正在下载...",img)
                    r = requests.get(img)
                    #img,'.jpg'
                    with open(r'.\\img' + (str(self.index)) + '.jpg', 'wb') as code:
                        code.write(r.content)
                        self.index += 1
                except:
                    input(print("下载出错!"))
                    exit(0)
            input(print('下载完成!!'))
            exit(0)
        return
    
    #视频下载
    def down_mp4(self,rid):
        try:
            r = requests.get(self.video_url + str(rid),headers=self.headers)
            res = etree.HTML(r.text)
            mp4_url=res.xpath('//video[@class="sogoke-video video-js"]/@src')
            if(mp4_url==[]):
                self.down_mp4(rid)
        except:
            #print("此资源为图片资源")
            pass
        else:
            for mp4 in mp4_url:
                try:
                    print("正在下载...",mp4)
                    r = requests.get(mp4)
                    with open(r'.\\video' + str((self.index)) + '.mp4', 'wb') as code:
                        code.write(r.content)
                        self.index += 1
                except:
                    input(print("下载出错!"))
                    exit(0)
            input(print('下载完成!!'))
            exit(0)
        return

if __name__ == "__main__":
    rid=input("输入文章ID:")
    kiinii(rid)
