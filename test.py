#!/usr/bin/env python
# -*- coding: utf_8 -*-
import requests

h = {
    'Host': '119.29.56.195:8080',
    'Content-Type': 'multipart/form-data; boundary=itcast',
    'Connection': 'keep-alive',
    'Accept': '*/*',
    'User-Agent': 'FamilyTree/1.2 CFNetwork/808.1.4 Darwin/16.1.0',
    'Content-Length': '86',
    'Accept-Language': 'zh-cn',
    'Accept-Encoding': 'gzip, deflate',

}
d = {"username": "15856691310",
     "password": "luhu199515lbh"}
r = requests.get("https://baidu.com")
print r.text.encode('gbk', 'ignore')
print r.status_code
