#! /usr/bin/env python
# coding=utf-8
'''
Created on 2013-4-19

@author: Ezio Ruan
'''

import urllib
import urllib2
from BeautifulSoup import BeautifulSoup
from doctor_config import DEPT_NAME_BOBY, TIME_DESC, ALL_DOCTORS, \
    DEPT_NAME_WOMAM, XMFY_CHOOSE_DESPEAK_URL, XMFY_DESPEAK_URL, XMFY_DESPEAK_FORM_URL



def read_url(url):
    opener = urllib2.build_opener()
    opener.addheaders = [('Accept-Charset', 'utf-8')]
    print 'GET', url
    
    url_response = opener.open(url)
    deal_html = url_response.read()
    soop = BeautifulSoup(deal_html)
    return soop


def post_url(url, param_dict):
    opener = urllib2.build_opener()
    opener.addheaders = [('Accept-Charset', 'utf-8')]
    print 'POST:', url
    data = encode_url_params(param_dict)
    url_response = opener.open(url, data)
    deal_html = url_response.read()
    soop = BeautifulSoup(deal_html)
    return soop



def encode_url_params(param_dict):
    param_dict = {key:value.encode('gb2312') for (key, value) in param_dict.iteritems() }
    params = urllib.urlencode(param_dict)
    return params




def get_choose_despeak_page(doctor_id, select_date, time_desc=TIME_DESC['MORNING'], dept_name=DEPT_NAME_BOBY):
    doctor = ALL_DOCTORS.get(doctor_id)
    param_dict = {'DOCTOR_ID':doctor_id, 'DOCTOR':doctor, 'SelectDate':select_date, 'TIME_DESC':time_desc, 'DEPT_NAME':dept_name}
    params = encode_url_params(param_dict)
    url = '%s?%s' % (XMFY_CHOOSE_DESPEAK_URL, params)
    return read_url(url)


def get_despeak_page(doctor_id, select_date, select_time, dept_name=DEPT_NAME_BOBY):
    doctor = ALL_DOCTORS.get(doctor_id)
    param_dict = {'DOCTOR_ID':doctor_id, 'DOCTOR':doctor, 'SelectDate':select_date, 'SelectTime':select_time, 'DEPT_NAME':dept_name}
    params = encode_url_params(param_dict)
    url = '%s?%s' % (XMFY_DESPEAK_URL, params)
    return  read_url(url)
    





def despeak(doctor_id, select_date, select_time, phone, icardid, username, dept_name=DEPT_NAME_BOBY,triage_no='330'):
    doctor = ALL_DOCTORS.get(doctor_id)
    param_dict = {'DOCTOR_ID':doctor_id, 'DOCTOR':doctor, 'SelectDate':select_date,
                  'SelectTime':select_time, 'DEPT_NAME':dept_name,'TRIAGE_NO':'triage_no','phone':phone,
                  'icardid':icardid, 'username':username,'ok': u' 查 询 ' }
    return post_url(XMFY_DESPEAK_FORM_URL, param_dict)
    

def is_success(soup):
    if str(soup.script).find('恭喜您预约成功') == -1:
        return False
    else:
        return True



def test_despeak():
#     soup = despeak('1144','2013-5-22','08:48','13625002107','350681198812051039',u'阮明辉',DEPT_NAME_WOMAM)
    

    
    time_list = ['08:05','08:10','08:15','08:20',
                '08:25', '08:30', '08:35', '08:40', '08:45',
                '08:50', '08:55', '09:00', '09:05', '09:10',
                '09:15', '09:20', '09:25', '09:30', '09:35', ]
    for time in time_list:
        soup = despeak('092', '2013-5-23', time, '15859251674', 'D75698209', u'石锦芬', DEPT_NAME_BOBY)
        result =  is_success(soup)
        if result:
            return True




def test_get_choose_despeak_page():
#    context = get_despeak_page('1263','2013-4-25',TIME_DESC['ALL_DAY'],DEPT_NAME_WOMAM)
#     context = get_choose_despeak_page('092', '2013-4-27')
    context = get_choose_despeak_page('1137', '2013-4-25')
    return context


def test_get_despeak_page():
    context = get_despeak_page('1263', '2013-4-26', '16:20', DEPT_NAME_WOMAM)
#     context = get_despeak_page('092','2013-4-27','8:00')
    return context    









if __name__ == '__main__':
#     print test_get_choose_despeak_page()
#     print test_get_despeak_page()
    print test_despeak()






    

















