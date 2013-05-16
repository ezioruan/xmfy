#! /usr/bin/env python
# coding=utf-8
'''
Created on 2013-4-19

@author: Ezio Ruan
'''

from bespeak import test_despeak
import time
import datetime
import thread

if __name__ == '__main__':
    while True:
        now =  datetime.datetime.now()
        print now
        time.sleep(1)
        hour = str(now).split()[1]
        if hour.startswith('19:58:00') or hour.startswith('19:59') or hour.startswith('20:00'):
             if test_despeak():
                 break
        elif hour.startswith('00:00'):
            break
