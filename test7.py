from time import sleep

__author__ = 'Administrator'
from appium import webdriver
desired_caps = { }

desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '5.1.1'
desired_caps['deviceName'] = 'MI red'
desired_caps['appPackage'] = 'net.luhu.mobilesafe'
desired_caps['appActivity'] = '.activity.HomeActivity'
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

sleep(1)
driver.find_element_by_id('net.luhu.mobilesafe:id/iv_icon').click()
sleep(1)
driver.find_element_by_id('net.luhu.mobilesafe:id/et_password').send_keys('luhu199515lbh')
driver.find_element_by_id('net.luhu.mobilesafe:id/btn_ok').click()
