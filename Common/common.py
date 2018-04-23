#!/usr/bin/env python
# -*- coding: utf-8 -*-
import urllib.request, urllib.parse
import xmltodict
import xmltojson, utils
import pprint, json

# 1.1 공공데이터포털에서 제공하는 오픈 API 요청 및 응답처리를 위한 함수입니다.
# 함수호출시 필요한 파라미터 : url(요청주소), params(요청변수)
def call_service(url, params):
    # print('Processing for call_service(url, params)')
    serviceKey = '9Y0U0be4B3TNGdq1Wr1Kigmw%2F5yVek4NpgDGvAMvw%2BrxWdTfbZqlLyRNZj%2BsMr0C1l3%2BF3twzwD6E%2BWt9ikzaQ%3D%3D'
    service = '%s?serviceKey=%s&%s' % (url, serviceKey, params)
    print(service)

    # Calling service
    r = urllib.request.urlopen(service)
    c = r.read().decode('utf-8')
    # print(c)

    return c

# 1.2 (1.1과 동일), 파라미터 : url, params, YN(화일저장 유무), fn(file name, 화일명)
def call_service(url, params, YN = None, fn = None):
    # print('Processing for call_service(url, params, YN = None, fn = None)')
    serviceKey = '9Y0U0be4B3TNGdq1Wr1Kigmw%2F5yVek4NpgDGvAMvw%2BrxWdTfbZqlLyRNZj%2BsMr0C1l3%2BF3twzwD6E%2BWt9ikzaQ%3D%3D'
    service = '%s?serviceKey=%s&%s' % (url, serviceKey, params)
    print(service)

    # Calling service
    r = urllib.request.urlopen(service)
    c = r.read().decode('utf-8')
    # print(c)

    # Writing file : 만약을 위해 화일을 생성해 둠
    if YN == 'Y':
        if fn == '':
            fn = 'samples.data'
        file = open(fn, 'w', encoding='utf-8')
        file.write(c)
        file.close()

    # Open & read file
    # file = open(fn, 'r', encoding='utf-8')
    # print(file.read())
    # file.close()

    return c

# 2. XML을 딕셔너리로 변환합니다.
# 파라미터 : c(XML contents)
def x2d(c):
    # print('Processing for XML to Dict')
    _dict = xmltodict.parse(c)
    # print(_dict)
    # item = _dict['response']['body']['items']['item']
    # print(item)

    return _dict

# 3. XML을 JSON으로 변환합니다.
# 파라미터 : c(XML contents)
def x2j(c):
    # print('Processing for XML to JSON')
    _json = xmltojson.parse(c)
    _djson = json.loads(_json)
    # pp = pprint.PrettyPrinter(indent=4)
    # pp.pprint(_djson)
    # items = _djson['response']['body']['items']['item']
    # pp.pprint(items)

    return _djson

# 4. 함수 시험용 : 추후 삭제 예정
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