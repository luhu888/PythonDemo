#!/usr/bin/env python
# -*- coding: utf_8 -*-
from selenium import webdriver
import time

dr = webdriver.Chrome()
dr.get('https://www.baidu.com')
dr.find_element_by_id('kw').send_keys('python')
dr.find_element_by_id('su').click()
dr.find_element_by_id('kw').clear()
time.sleep(5)
dr.quit()











