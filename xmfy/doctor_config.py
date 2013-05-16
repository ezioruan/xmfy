#! /usr/bin/env python
# coding=utf-8
'''
Created on 2013-4-19

@author: Ezio Ruan
'''


XMFY_URL = 'http://www.xmfybj.cn/yy/' #预约系统主页
XMFY_CHOOSE_DESPEAK_URL = 'http://www.xmfybj.cn/yy/mainP.asp' #选择医生和时间进入预约系统
XMFY_DESPEAK_URL = 'http://www.xmfybj.cn/yy/login.asp' #预约界面
XMFY_DESPEAK_FORM_URL = 'http://www.xmfybj.cn/yy/loginchk.asp' #预约表单提交


ALL_DOCTORS = {
    #产科所有的主任
    '092':u'钟红秀',
    '1137':u'张雪芹',
    '022':u'杨华',
    '158':u'吴琦嫦',
    '0873':u'李丽榕',
    #妇科的医生，测试用
    '1263':u'钟晓燕',
    '1144':u'骆亚平',
    '042':u'曹雅琴',
    
}


TIME_DESC = {
    'MORNING':u'上午',
    'AFTERNOON':u'下午',
    'ALL_DAY':u'全天',

}

DEPT_NAME_BOBY = u'产科门诊'
DEPT_NAME_WOMAM = u'妇科门诊'