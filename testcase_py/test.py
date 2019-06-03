#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
import json

url = 'http://221.122.92.15:11000/ai-access/nlp?engine=MusicBox&needcontent=yes'
print(url)
body = {"LIBaseinfo":{"query":"apple","contextid":""},"opmode":"remote"}
print(body)
headers = {'appId': "MB-STEST-0002", 'appVersion': "2016060401",
           'clientId':"000000000000000-e8206604ed45",'sequenceId':"08002700DC94-15110519074300001",
           'accessToken':"TGTX34LCQSHE1QF2D0GGAHUGSHGT00",'sign':"bd4495183b97e8133aeab2f1916fed41",
           'timestamp':"654323456432434",'language':"zh-cn",'timezone':"8",
           'Content-Type':"application/json",'deviceid':"DC62C2B7BE03DD9C10D07AF23CC8"}
print(headers)
try:
    requests.adapters.DEFAULT_RETRIES = 15
    # 设置连接活跃状态为False
    s = requests.session()
    s.keep_alive = False
    response = requests.post(url, data = json.dumps(body), headers = headers,stream= False,timeout= 10)
    response.close()
    del(response)
except Exception as e:
    print(e)

#print(response.text)
# 返回响应头
#print(response.status_code)
#requests.close()
