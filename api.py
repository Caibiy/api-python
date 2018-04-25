#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date		:2018年4月25日10:14:14

import base64
import datetime
import hashlib
import hmac
import json
import urllib
import urllib.parse
import urllib.request
import requests

'''
APIKEY
'''
ACCESS_KEY = "4074ad98-8930-4c61-a792-1c3a0a934cad"
SECRET_KEY = "11fbe35be5331bc4d6a96dda4604dd272d5d006d"

API_URL = "https://api.exx.com/data/v1/"
TRADE_URL = "https://trade.exx.com/api/"

def http_get_request(url, params, add_to_headers=None):
    headers = {
        "Content-type": "application/x-www-form-urlencoded",
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36',
    }
    if add_to_headers:
        headers.update(add_to_headers)
    postdata = urllib.parse.urlencode(params)
    response = requests.get(url, postdata, headers=headers, timeout=5) 
    try:
        
        if response.status_code == 200:
            return response.json()
        else:
            return
    except BaseException as e:
        print("httpGet failed, detail is:%s,%s" %(response.text,e))
        return

def getMarkets():
	url = API_URL+'markets'
	params = {}
	return http_get_request(url,params)

if __name__ =='__main__':
	print(getMarkets())
	