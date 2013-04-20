#! /usr/bin/env python
# coding=utf-8
'''
Created on 2013-4-19

@author: Ezio Ruan
'''

from bespeak import test_despeak
import time

if __name__ == '__main__':
    for i in range(100):
        test_despeak()
        time.sleep(1)