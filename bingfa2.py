#!/usr/bin/env python
# -*- coding: utf_8 -*-
import requests
import datetime
import time
import threading


class url_request():
    times = []
    error = []

    def req(self, AppID, url):
        myreq = url_request()
        headers = {'User-Agent': 'Mozilla/5.0 (Linux; Android 4.2.1; en-us; Nexus 4 Build/JOP40D)'
                                 ' AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Mobile Safari/535.19'}
        payload = {'AppID': AppID, 'CurrentURL': url}
        r = requests.post("http://xx.xxx.com/WeiXinJSAccessToken/json/WeChatJSTicket", headers=headers, data=payload)
        ResponseTime = float(r.elapsed.microseconds)/1000     # ��ȡ��Ӧʱ�䣬��λms
        myreq.times.append(ResponseTime)    # ����Ӧʱ��д������
        if r.status_code != 200:
            myreq.error.append("0")
if __name__ == '__main__':
    myreq = url_request()
    threads = []
    starttime = datetime.datetime.now()
    print "request start time %s" % starttime
    nub = 50    # ���ò����߳���
    ThinkTime = 0.5     # ����˼��ʱ��
    for i in range(1, nub+1):
        t = threading.Thread(target=myreq.req, args=('12', 'http://m.ctrip.com/webapp/cpage/#mypoints'))
        threads.append(t)
    for t in threads:
        time.sleep(ThinkTime)
        # print "thread %s" %t #��ӡ�߳�
        t.setDaemon(True)
        t.start()
    t.join()
    endtime = datetime.datetime.now()
    print "request end time %s" % endtime
    time.sleep(3)
    AverageTime = "{:.3f}".format(float(sum(myreq.times))/float(len(myreq.times)))    # ���������ƽ��ֵ������3λС��
    print "Average Response Time %s ms" % AverageTime   # ��ӡƽ����Ӧʱ��
    usetime = str(endtime - starttime)
    hour = usetime.split(':').pop(0)
    minute = usetime.split(':').pop(1)
    second = usetime.split(':').pop(2)
    totaltime = float(hour)*60*60 + float(minute)*60 + float(second)    # �����ܵ�˼��ʱ��+����ʱ��
    print "Concurrent processing %s" % nub    # ��ӡ������
    print "use total time %s s" % (totaltime-float(nub*ThinkTime))    # ��ӡ�ܹ����ĵ�ʱ��
    print "fail request %s" % myreq.error.count("0")     # ��ӡ����������
