#!/usr/bin/env python
# -*- coding: utf-8 -*-
import urllib.request, urllib.parse
import xmltodict
import xmltojson, utils
import pprint, json
import os, time

# serviceKey를 global로 관리
def get_serviceKey():
    # serviceKey = '9Y0U0be4B3TNGdq1Wr1Kigmw%2F5yVek4NpgDGvAMvw%2BrxWdTfbZqlLyRNZj%2BsMr0C1l3%2BF3twzwD6E%2BWt9ikzaQ%3D%3D' # '오픈 API 신청하고 받은 키를 입력하세요.'
    serviceKey = '8iN1bBSDMvTrKvFns%2FE2xJ4%2BNCOAEdNrvdQ%2BR%2FBLGyEhv3%2BdSruGH0GkmeszfEZk6Y4w15uvJNI9x6u3nPmX1g%3D%3D' # 2018-05-28 재발급
    return serviceKey

# 1.1 공공데이터포털에서 제공하는 오픈 API 요청 및 응답처리를 위한 함수입니다.
# 함수호출시 필요한 파라미터 : url(요청주소), params(요청변수)
def call_service(url, params):
    # print('Processing for call_service(url, params)')
    # service = '%s?serviceKey=%s&%s' % (url, get_serviceKey(), params)
    service = '%s?%s' % (url, params)
    print(service)

    # 오픈 API 호출
    try:
        r = urllib.request.urlopen(service)
        c = r.read().decode('utf-8')
        # print(c)

        return c
    except Exception as e:
        print(str(e))

# 1.2 (1.1과 동일), 파라미터 : url, params, YN(화일저장 유무), fn(file name, 화일명)
def call_serviceF(url, params, YN = None, fn = None):
    try:
        c = call_service(url, params)

        # Writing file : 만약을 위해 화일을 생성해 둠
        if YN == 'Y':
            create_file(c, fn)

        return c
    except Exception as e:
        print(str(e))

# 2-1. XML을 딕셔너리로 변환합니다.
# 파라미터 : c(XML contents)
def x2d(c):
    # print('Processing for XML to Dict')
    try:
        _dict = xmltodict.parse(c)
        # print(_dict)
        # item = _dict['response']['body']['items']['item']
        # print(item)

        return _dict
    except Exception as e:
        print(str(e))

# 2-2. XML을 JSON으로 변환합니다.
# 파라미터 : c(XML contents)
def x2j(c):
    # print('Processing for XML to JSON')
    try:
        _json = xmltojson.parse(c)
        _djson = json.loads(_json)
        # pp = pprint.PrettyPrinter(indent=4)
        # pp.pprint(_djson)
        # items = _djson['response']['body']['items']['item']
        # pp.pprint(items)

        return _djson
    except Exception as e:
        print(str(e))

# 3. JSON을 딕셔너리로 변환합니다.
# 파라미터 : c(JSON contents)
def j2d(c):
    # print('Processing for XML to Dict')
    try:
        _json = json.loads(c)
        # print(_json)
        # item = _json['response']['body']['items']['item']
        # print(item)

        return _json
    except Exception as e:
        print(str(e))

# 4. Created file
def create_file(content, fn = None):
    if (fn == None):
        fn = os.getcwd() + '/data/' + str(int(round(time.time() * 1000)))

    file = open(fn, 'w', encoding='utf-8')
    file.write(content)
    file.close()

    # Open & read file
    file = open(fn, 'r', encoding='utf-8')
    print(file.read())
    file.close()

# 5. 함수 시험용 : 추후 삭제 예정
def hello():
    return 'Hello, World!!!'

# common.py에서 필요한 메모 : 추후 삭제 예정
'''
NumPy, pandas, matplotlib, IPython, SciPy
statsmodels, PyTables, PyQt, PySide, xlrd, lxml, basemap, pymongo, requests
PyPi, http://pypi.python.org/
https://docs.python.org/3/library/statistics.html
https://matplotlib.org/api/_as_gen/matplotlib.pyplot.plot.html
https://matplotlib.org/gallery/pyplots/pyplot_text.html#sphx-glr-gallery-pyplots-pyplot-text-py
https://matplotlib.org/gallery/pyplots/pyplot_text.html#sphx-glr-gallery-pyplots-pyplot-text-py
https://matplotlib.org/gallery/misc/table_demo.html#sphx-glr-gallery-misc-table-demo-py
https://plot.ly/matplotlib/histograms/
http://pinkwink.kr/956
'''

if __name__ == "__main__":
#    c = ['<?xml version="1.0" encoding="UTF-8" standalone="yes"?><friends><friend number="01"><name>철수</name><height>180</height></friend><friend number="02"><name>영희</name><height>163</height></friend></friends>']
#    _djson = x2j(c[0])
#    friend = _djson['friends']
#    pprint.pprint(friend)
    create_file('adfadfadsfa')