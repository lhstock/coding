# !/usr/bin/env python
# -*- coding:utf-8 -*-
import urlparse
import json
from cgi import parse_qs,escape
def application(environ,start_response):
    start_response('200 OK',[('Content-Type','text/html')])
    params = parse_qs(environ['QUERY_STRING'])
    name = params.get('name',[''])[0]
    website = params.get('website',[''])[0]
    user = params.get('user',[''])[0]
    dic = [{'name':name,'website':website,"user":user}]
    data = {'data':dic}
    return json.dumps(data)