#!/usr/bin/env python
# -*- coding: utf_8 -*-
import random
import requests
import datetime
import time
import threading
import number
'''并发测试API'''


class url_request():
    times = []
    error = []

    def req(self, name, password, gender):
        myreq = url_request()
        headers = {}
        payload = {"username": name, "password": password, "gender": gender}
        r = requests.post("http://192.168.1.102:8000/user/", headers=headers, data=payload)
        # print r.status_code
        # print name
        ResponseTime = float(r.elapsed.microseconds)/1000     # 获取响应时间，单位ms
        myreq.times.append(ResponseTime)    # 将响应时间写入数组
        if r.status_code != 200:
            myreq.error.append("0")


if __name__ == '__main__':
    myreq = url_request()
    threads = []
    starttime = datetime.datetime.now()
    print "request start time %s" % starttime

    nub = 10    # 设置并发线程数
    ThinkTime = 0.5     # 设置思考时间
    for i in range(1, nub+1):
        name = number.full_name()
        password = number.gennerator()
        gender = random.randint(0, 1)
        t = threading.Thread(target=myreq.req, args=(name, password, gender))
        threads.append(t)
    for t in threads:
        time.sleep(ThinkTime)
        # print "thread %s" % t   # 打印线程
        t.setDaemon(True)
        t.start()
    t.join()
    endtime = datetime.datetime.now()
    print "request end   time %s" % endtime
    time.sleep(3)
    AverageTime = "{:.3f}".format(float(sum(myreq.times))/float(len(myreq.times)))    # 计算数组的平均值，保留3位小数
    print "平均响应时长 %s ms" % AverageTime   # 打印平均响应时间
    usetime = str(endtime - starttime)
    hour = usetime.split(':').pop(0)
    minute = usetime.split(':').pop(1)
    second = usetime.split(':').pop(2)
    totaltime = float(hour)*60*60 + float(minute)*60 + float(second)    # 计算总的思考时间+请求时间
    print "并发数 %s" % nub    # 打印并发数
    print "总耗时 %s s" % (totaltime-float(nub*ThinkTime))    # 打印总共消耗的时间
    print "请求失败数 %s" % myreq.error.count("0")     # 打印错误请求数
