#!/usr/bin/env python
# -*- coding: utf_8 -*-
from selenium import webdriver
import time

dr = webdriver.Chrome()
dr.get('http://192.168.1.102/api/#/index')
dr.find_element_by_id('username_input_js').send_keys('luhu')
dr.find_element_by_name('password').send_keys('luhu199515lbh')
dr.find_element_by_css_selector('button.eo-button-success.index-btn').click()
time.sleep(1)
dr.find_element_by_css_selector('th.ng-binding').click()
time.sleep(1)
dr.find_element_by_css_selector('td.second-th.ng-binding').click()
time.sleep(1)
dr.find_element_by_css_selector('li.pull-left.switch-test').click()
time.sleep(1)
