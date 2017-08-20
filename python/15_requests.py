# !/usr/bin/env python
#-*-coding:utf-8-*-
import requests
cs_url  = 'https://api.github.com'
cs_user = '532351163@qq.com'
cs_psw  = 'code1004'

r = requests.get(cs_url, auth=(cs_user, cs_psw))
print 'sdk:',r.status_code,requests.codes.ok
if r.status_code == requests.codes.ok :
    for k, v in r.json().items():
        print k, v
