#! /usr/bin/env python
# coding=utf-8
'''
Created on 2013-4-19

@author: Ezio Ruan
'''
a = 'mainP.asp?DOCTOR_ID=1263&DOCTOR=%D6%D3%CF%FE%D1%E0&SelectDate=2013-4-25&TIME_DESC=%C8%AB%CC%EC&DEPT_NAME=%B8%BE%BF%C6%C3%C5%D5%EF'
b = 'mainP.asp?DOCTOR_ID=1263&DOCTOR=钟晓燕&SelectDate=2013-4-25&TIME_DESC=全天&DEPT_NAME=妇科门诊'


import urllib



c = u'钟晓燕'.encode('gb2312')
d = '%D6%D3%CF%FE%D1%E0'

print urllib.quote(c)
print urllib.urlencode({'c':c})


