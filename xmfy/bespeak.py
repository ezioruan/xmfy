#! /usr/bin/env python
# coding=utf-8
'''
Created on 2013-4-19

@author: Ezio Ruan
'''

import urllib
import urllib2
from BeautifulSoup import BeautifulSoup
from doctor_config import DEPT_NAME_BOBY, TIME_DESC, ALL_DOCTORS,\
    DEPT_NAME_WOMAM,XMFY_CHOOSE_DESPEAK_URL



def read_url(url):
    opener = urllib2.build_opener()
    opener.addheaders = [('Accept-Charset', 'utf-8')]
    print url
    
    url_response = opener.open(url)
    deal_html = url_response.read()
    return deal_html

def get_choose_despeak_page(doctor_id,select_date,time_desc=TIME_DESC['MORNING'],dept_name=DEPT_NAME_BOBY):
    doctor = ALL_DOCTORS.get(doctor_id)
    data = {'DOCTOR_ID':doctor_id,'DOCTOR':doctor,'SelectDate':select_date,'TIME_DESC':time_desc,'DEPT_NAME':dept_name}
    data = {key:value.encode('gb2312') for (key,value) in data.iteritems() }
    params = urllib.urlencode(data)
    print params
    url = '%s?%s' % (XMFY_CHOOSE_DESPEAK_URL,params)
    return read_url(url)




def despeak():
#    context = get_despeak_page('1263','2013-4-25',TIME_DESC['ALL_DAY'],DEPT_NAME_WOMAM)
    context = get_choose_despeak_page('092','2013-4-27')
    soup = BeautifulSoup(context)
    print soup
    


if __name__ == '__main__':
    despeak()






    

















