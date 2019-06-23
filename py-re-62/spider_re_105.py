#!/usr/bin/env python  
# -*- coding: utf-8 -*-
"""
@author: zhangslob
@file  : test.py
@time  : 2019-04-11
@desc  :

"""

import requests

headers = {
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
    'Referer': 'https://www.lagou.com/',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,zh-TW;q=0.7',
}

params = (
    ('labelWords', ''),
    ('fromSearch', 'true'),
    ('suginput', ''),
)
s = requests.Session()
s.headers.update(headers)

response = s.get('https://www.lagou.com/jobs/list_python', params=params)

data = {
    'first': 'true',
    'pn': '1',
    'kd': 'python'
}

r = s.post('https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false', data=data, headers={
    'Origin': 'https://www.lagou.com',
    'X-Anit-Forge-Code': '0',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Referer': 'https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput=',
    'X-Requested-With': 'XMLHttpRequest',
    'X-Anit-Forge-Token': 'None',
})
print(r.text)