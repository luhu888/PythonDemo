#!/usr/bin/env python
# -*- coding: utf_8 -*-
from splinter import Browser # Visit URL
import time

url = "https://www.baidu.com"
b = Browser('chrome')
b.visit(url)
b.find_by_id('kw').fill('python')
time.sleep(3)     # Find and click the 'search' button
button = b.find_by_id('su')   # Interact with elements
button.click()
