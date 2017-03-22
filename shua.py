#!/usr/bin/env python
# -*- coding: utf_8 -*-
import random
import unittest
import requests
import number


for i in range(1, 20):
    gender = random.randint(0, 1)
    name = number.full_name()
    password = number.gennerator()
    headers = {}
    url = 'http://192.168.1.105:8000/user/'
    data = {
        "username": name,
        "password": password,
        "gender": gender
        }
    r = requests.post(url=url, json=data, headers=headers)
    print r.text
    print r.status_code


class MyTest(unittest.TestCase):
    def setUp(self):
        print 'start test'
        pass

    def tearDown(self):
        print 'end test'
        pass
