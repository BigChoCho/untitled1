
from urllib import request
from lxml import etree

import json

#词汇表
words = []


def shanbei(page):
    url = "https://www.shanbay.com/wordlist/104899/202159/?page=%s"%page

    rsp = request.urlopen(url)

    html = rsp.read().decode()
    # print(html)
    html = etree.HTML(html)
    trhtml = html.xpath("//tr")
    print(trhtml)
    for tr in trhtml:
        '''
        查相应的单词和介绍
        '''
        word = {}
        #當前節點的任一地方
        strong = tr.xpath('.//strong')
        # 有長度代表存在
        if len(strong):
            # strip把找到的内容去掉空格
            name = strong[0].text.strip()
            word['name'] = name

        # 查找单词的释义
        #./td=根目錄("//tr")下找td
        td_content = tr.xpath('./td[@class="span10"]')
        if len(td_content):
            content = td_content[0].text.strip()
            word['content'] = content

        print(word)

        if word != {}:
            #存入數組內
            words.append(word)
    print(words)

if __name__ == '__main__':
    shanbei(2)