#!/usr/bin/env python
# coding=utf-8
"""
Filename:       grap.py
Last modified:  2015-10-16 15:43

Description:

"""
from BeautifulSoup import BeautifulSoup
import codecs
import json
import urlparse


def qs(url):
    query = urlparse.urlparse(url).query
    return dict([(k, v[0]) for k, v in urlparse.parse_qs(query).items()])


def save_file(data, file_name):
    with codecs.open(file_name, 'w', 'utf-8') as f:
        f.write(json.dumps(data))


def clean_text(text):
    new_text = text.replace(')', '').replace('"', '')
    return new_text


def grap_doctors():
    # grap the new html if need
    # http://yy.xmfybj.cn/
    with codecs.open('doctors.html', 'r', 'gbk') as f:
        soup = BeautifulSoup(f.read())
        doctors = []
        depts = []
        for li in soup.findAll('li'):
            href = li.a.get('href')
            url_values = qs(href)
            doctors.append({
                'doctor_code': url_values['DOCTOR_CODE'],
                'dept_code': url_values['DEPT_CODE'],
                'doctor_name': li.text,
            })
        for a in soup.findAll('a', 'stit col-d9'):
            _, dept_code, dept_name = a.get('onclick').split(',')
            depts.append({
                'dept_code': clean_text(dept_code),
                'dept_name': clean_text(dept_name),
            })
        save_file(doctors, 'doctors.json')
        save_file(depts, 'depts.json')


if __name__ == "__main__":
    grap_doctors()
