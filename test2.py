#!/usr/bin/env python
# -*- coding: utf_8 -*-
import requests

p = {
    "username": "15856691310",
    "password": "e10adc3949ba59abbe56e057f20f883e",
}
r = requests.post("http://familytree.dreamgo.tech/user/login/", data=p)
print r.text
print r.status_code
h = {'Authorization': 'Token 44a0ff921bf0ea4ba6251a970acc4aca47ef71b8'}
w = requests.get("http://familytree.dreamgo.tech/user/40/", headers=h)
print w.text.encode('gbk')
print w.status_code
z = requests.get("http://familytree.dreamgo.tech/static/h5/familyTree.html")
print z.text.encode('gbk')
print z.status_code


