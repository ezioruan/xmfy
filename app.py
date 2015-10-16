#!/usr/bin/env python
# coding=utf-8
"""
Filename:       app.py
Last modified:  2015-10-16 16:48

Description:

"""
from setting import HTTP_HOST, HTTP_PORT
from flask import Flask 
import json
from gevent.pywsgi import WSGIServer
from data import data_manager


app = Flask(__name__)


@app.route('/doctors/<dept_code>')
def doctors_by_dept_code(dept_code):
    return json.dumps(data_manager.doctors)


@app.route('/doctors')
def doctors():
    return json.dumps(data_manager.doctors)


@app.route('/depts')
def depts():
    return json.dumps(data_manager.depts)


def run_web_server():
    server = WSGIServer((HTTP_HOST, HTTP_PORT), app,)
    server.serve_forever()


if __name__ == "__main__":
    run_web_server()
