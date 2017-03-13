#!/usr/bin/env python
# -*- coding: utf_8 -*-
import requests

p = {
    "loginName": "luhu",
    "loginPasssword": "bbafa7999e009f6cf877906bf72dad95"
    }
r = requests.post("http://192.168.1.102/api/server/index.php?g=Web&c=Guest&o=login", data=p)
print r.text.encode('utf-8')
print r.status_code
z = requests.get("http://192.168.1.102/api/#/project/api/test?projectID=4&groupID=-1&apiID=7")

print z.status_code
print z.text.encode('utf-8')