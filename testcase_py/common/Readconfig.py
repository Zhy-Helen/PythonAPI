# -*- coding:utf-8 -*-
import os
def get_API_url(api_name):
    fp = open(os.getcwd()+"\\API_URL.txt")
    api_infos = fp.readlines()
    # 通过for循环来遍历配置文件里的每一个url，并且返回传入的接口名称相应的url
    for api in api_infos:
        # 去除因为读取产生的换行空格等
        api_f = api.strip(' \r\n\t')
        api_c = api_f.split('=',1)
        if api_name == api_c[0]:
            return api_c[1]
