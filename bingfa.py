#!/usr/bin/env python
# -*- coding: utf_8 -*-
import threading, time, httplib
HOST = "192.168.1.102";    # ������ַ ����192.168.1.101
PORT = 80    # �˿�
URI = "/api/#/index"    # ��Ե�ַ,�Ӳ�����ֹ���棬������ܻ᷵��304
TOTAL = 0   # ����
SUCC = 0    # ��Ӧ�ɹ���
FAIL = 0    # ��Ӧʧ����
EXCEPT = 0  # ��Ӧ�쳣��
MAXTIME = 0    # �����Ӧʱ��
MINTIME = 100    # ��С��Ӧʱ�䣬��ʼֵΪ100��
GT3 = 0    # ͳ��3������Ӧ��
LT3 = 0     # ͳ�ƴ���3����Ӧ��
# ����һ�� threading.Thread ��������


class RequestThread(threading.Thread):
    # ���캯��
    def __init__(self, thread_name):
        threading.Thread.__init__(self)
        self.test_count = 0

    # �߳����е���ں���
    def run(self):

        self.test_performace()

    def test_performace(self):
            global TOTAL
            global SUCC
            global FAIL
            global EXCEPT
            global GT3
            global LT3
            try:
                st = time.time()
                conn = httplib.HTTPConnection(HOST, PORT, False)
                conn.request('GET', URI)
                res = conn.getresponse()
                # print 'version:', res.version
                # print 'reason:', res.reason
                # print 'status:', res.status
                # print 'msg:', res.msg
                # print 'headers:', res.getheaders()
                start_time
                if res.status == 200:
                    TOTAL += 1
                    SUCC += 1
                else:
                    TOTAL += 1
                    FAIL += 1
                time_span = time.time()-st
                print '%s:%f\n' % (self.name, time_span)
                self.maxtime(time_span)
                self.mintime(time_span)
                if time_span > 3:
                    GT3 += 1
                else:
                    LT3 += 1
            except Exception, e:
                print e
                TOTAL += 1
                EXCEPT += 1
            conn.close()

    def maxtime(self, ts):
            global MAXTIME
            print ts
            if ts > MAXTIME:
                MAXTIME = ts

    def mintime(self, ts):
            global MINTIME
            if ts < MINTIME:
                MINTIME = ts

# main ���뿪ʼ
print '===========task start==========='
# ��ʼ��ʱ��
start_time = time.time()
# �������߳���
thread_count = 29

i = 0
while i <= thread_count:
    t = RequestThread("thread" + str(i))
    t.start()
    i += 1
t = 0
# ���������ж���ɻ����50��ͽ���
while TOTAL < thread_count | t > 50:
        print "total:%d,succ:%d,fail:%d,except:%d\n" % (TOTAL, SUCC, FAIL, EXCEPT)
        print HOST, URI
        t += 1
        time.sleep(1)
print '===========task end==========='
print "total:%d,succ:%d,fail:%d,except:%d"%(TOTAL, SUCC, FAIL, EXCEPT)
print 'response maxtime:', MAXTIME
print 'response mintime', MINTIME
print 'great than 3 seconds:%d,percent:%0.2f' % (GT3, float(GT3)/TOTAL)
print 'less than 3 seconds:%d,percent:%0.2f' % (LT3, float(LT3)/TOTAL)