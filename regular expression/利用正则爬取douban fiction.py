# -*- coding: utf-8 -*-
"""
Created on Mon Jun 18 16:07:30 2018

@author: Ezreal

利用正则表达式(regex),爬取douban小说的链接、书名、作者
如：
    https://read.douban.com/ebook/958945/ 三体全集 刘慈欣
    https://read.douban.com/ebook/34157247/ 月亮与六便士 〔英〕毛姆
    https://read.douban.com/ebook/30712317/ 杀死一只知更鸟 〔美〕哈珀·李
    https://read.douban.com/ebook/46023318/ 房思琪的初恋乐园 林奕含

"""

import re
import requests

#创建Session，维持对话
s = requests.Session()

#定义函数，给予url，返回一个html
def getHTML(url,code='utf-8'):
    try:
        r = s.get(url,timeout=20)
        r.raise_for_status()
        r.encoding = code
        return r.text
    except:
        print('getHTML Error')

#定义运行函数：利用regex爬取我们想要的数据，如：url、书名、作者
def startRUN(start_page,end_page):
    for page in range(start_page,end_page+1):
        try:
            try:
                #构建一个URL
                page_url = 'https://read.douban.com/kind/100?start='+str(page*20)+'&sort=hot&promotion_only=False&min_price=None&max_price=None&works_type=None'
                html = getHTML(page_url)
                #利用re.compile()构建一个Regex
                pattern = re.compile('<div class="title">.*?<a href="(.*?)">(.*?)</a>.*?<span class="labeled-text">.*?<a class="author-item" href=.*?>(.*?)</a>',re.S)
                #利用re.findall()找到所有符合条件的信息
                regular_content = re.findall(pattern,str(html))
            except:
                print('regex error')
            
            #迭代
            for items in regular_content:
                url,name,author = items
                #利用re.sub()替代
                url = re.sub('^','https://read.douban.com',url)
                print(url,name,author)
        except:
            print('startRUN Error')

#定义主函数           
def main():
    start_page = int(input('please input beginning page:'))
    end_page = int(input('please input ending page:'))
    startRUN(start_page,end_page)
    
if __name__ =='__main__':
    main()