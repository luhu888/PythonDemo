#!/usr/bin/env python
# -*- coding: utf_8 -*-
import random
import requests
import number


for i in range(1, 20):
    gender = random.randint(0, 1)
    name = number.full_name()
    password = number.gennerator()
    p = {
        "username": name,
        "password": password,
        "gender": gender
        }
    r = requests.post("http://192.168.1.102:8000/user/", data=p)
    print r.text
    print r.status_code
