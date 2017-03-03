#!/usr/bin/env python
# -*- coding: utf_8 -*-
from splinter import Browser
import time

with Browser('chrome') as browser:    # 打开chrome流浪器，如果一切正常，就将其作为browser，当函数完成时，关闭浏览器
    url = "https://www.baidu.com"
    browser.visit(url)
    browser.find_by_id('kw').fill('python')
    # Find and click the 'search' button
    button = browser.find_by_id('su')
    # Interact with elements
    button.click()
    time.sleep(20)
