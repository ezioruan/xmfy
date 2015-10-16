#!/usr/bin/env python
# coding=utf-8
"""
Filename:       data.py
Last modified:  2015-10-16 16:43

Description:

"""

import json
import codecs


def read_from_file(file_name):
    with codecs.open(file_name, 'r', 'utf-8') as f:
        content = json.loads(f.read())
        print content
        return content


class DataManager(object):

    def __init__(self):
        self.doctors = read_from_file('doctors.json')
        self.depts = read_from_file('depts.json')

    def get_doctors(self, dept_code):
        return [doctor for doctor in self.doctors if doctor['dept_code'] == dept_code]


data_manager = DataManager()
