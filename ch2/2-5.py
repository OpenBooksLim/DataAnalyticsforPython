# Step 1. 필요한 모듈을 import합니다.
# -*- coding: utf-8 -*-
import common.common as cm
import pprint as pp
import statistics as st
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
rc('font', family=font_name)
import os
import numpy as np
from matplotlib import pyplot

# Step 2. 관광지숙박정보목록조회를 위한 요청변수 및 요청주소 등을 구성합니다.
url = 'http://openapi.jbfood.go.kr:8080/openapi/service/TouristAccoService/getTouristAcco' # 관광지숙박정보목록조회

# area = 01-고창군 02-군산시 03-김제시 04-남원시 05-무주군 06-부안군 07-순창군 08-완주군 09-익산시 10-임실군 11-장수군 12-전주시 13-진안군 14-진안군
area = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14']
# category = 01-호텔 02-굿스테이 03-리조트/콘도 04-모텔 05-팬션/민박 06-유스호스텔/수련원 07-한옥
category = ['01', '02', '03', '04', '05', '06', '07']
c = []
for i in range(0, len(area)):
    for j in range(0, len(category)):
        params = 'serviceKey=%s&Area=%s&Category=%s' % (cm.get_serviceKey(), area[i], category[j])
        print('params : ', params)

        # 서비스 호출시 지역/분류별로 화일을 생성합니다. 저장할 화일명을 정의합니다.
        fn = os.getcwd() + '/data/' + '2-5_%s.da' % (str(area[i]) + str(category[j]))
        _c = cm.call_serviceF(url, params, 'Y', fn)
        c.append(_c)

print(c)

# Step 3. 관광지숙박정보상세보기조회를 위하여 관광지숙박정보목록조회의 결과에서 sno를 추출합니다.
pp = pp.PrettyPrinter(indent=4)
data = []
for i in range(0, len(c)):
    try:
        # 응답값이 XML일 경우
        _djson = cm.x2j(c[i])
        item = _djson['response']['body']['items']['item']
        if (isinstance(item, list)):
            pp.pprint(item)
            data.extend(item)
    except Exception as e:
        continue
pp.pprint(data)

sno = []
i = 0
for v in data:
    i += 1
    sno.append(int(v['sno']))
print('sno::: ', sno)

# Step 4. 관광지숙박정보상세보기조회를 위한 요청변수 및 요청주소 등을 구성합니다.
url = 'http://openapi.jbfood.go.kr:8080/openapi/service/TouristAccoService/getTouristAccoDetail' # 관광지숙박정보상세보기조회
for i in range(0, len(sno)):
    params = 'serviceKey=%s&SNO=%s' % (cm.get_serviceKey(), sno[i])
    print('params : ', params)

    # 서비스 호출
    _c = cm.call_service(url, params)
    # 필요시 화일을 생성합니다. 저장할 화일명을 정의합니다.
    fn = os.getcwd() + '/data/' + '2-5(sno)_%s.da' % str(sno[i])
    cm.create_file(_c, fn)
    c.append(_c)

print(c)

# Step 5. item의 구조를 분석하고, 분석하고자 하는 값들을 추출하기 위한 데이터를 전처리합니다.
data2 = []
for i in range(0, len(c)):
    try:
        # 응답값이 XML일 경우
        _djson = cm.x2j(c[i])
        item = _djson['response']['body']['item']

        if (isinstance(item, dict)):
            pp.pprint(item)
            data2.append(item)
    except Exception as e:
        continue

pp.pprint(data2)

# build : 건물수, room : 객실수, checkIn : 체크인, checkOut : 체크아웃
stat = np.empty((0, 4), int)

i = 0
for v in data2:
    i += 1
    stat = np.vstack([stat, np.array([int(v['build']), int(v['room']), int(v['checkIn']), int(v['checkOut'])])])
print('stat::: ', stat)
print('build::: ', stat[:, 0])
print('room::: ', stat[:, 1])
print('checkIn::: ', stat[:, 2])
print('checkOut::: ', stat[:, 3])

# Step 6. 데이터(건물수, 객식수, 체크인, 체크아웃) 분석을 수행합니다.
# Step 6-1. statistics를 활용한 통계량 분석
try:
    print('mean:::', st.mean(map(float, stat[:, 1])))
    print('harmonic_mean:::', st.harmonic_mean(map(float, stat[:, 1])))
    print('median:::', st.median(map(float, stat[:, 1])))
    print('median_low:::', st.median_low(map(float, stat[:, 1])))
    print('median_high:::', st.median_high(map(float, stat[:, 1])))
    print('median_grouped:::', st.median_grouped(map(float, stat[:, 1])))
    print('pstdev:::', st.pstdev(map(float, stat[:, 1])))
    print('stdev:::', st.stdev(map(float, stat[:, 1])))
    print('pvariance:::', st.pvariance(map(float, stat[:, 1])))
    print('variance:::', st.variance(map(float, stat[:, 1])))
except Exception as e:
    print(str(e))

# Step 7. 분석을 위한 표본에 대하여 시각화를 진행합니다.
# Step 7-1. Four polar axes
a = np.trim_zeros(stat[:, 0])
b = np.trim_zeros(stat[:, 1])
c = np.trim_zeros(stat[:, 2])
d = np.trim_zeros(stat[:, 3])

f, axarr = plt.subplots(2, 2, subplot_kw=dict(projection='polar'))
axarr[0, 0].plot(a, b)
axarr[0, 0].set_title('build/room plot')
axarr[0, 1].scatter(a, b)
axarr[0, 1].set_title('build/room scatter')
axarr[1, 0].plot(c, d)
axarr[1, 0].set_title('checkIn/checkOut plot')
axarr[1, 1].scatter(c, d)
axarr[1, 1].set_title('checkIn/checkOut scatter')
f.subplots_adjust(hspace=0.3)
plt.show()

# Step 7-2. Multiple histogram
bins = np.linspace(0, 24, 30)
pyplot.style.use('seaborn-deep')
# pyplot.hist([a, b, c, d], bins, label=['build', 'room', 'checkIn', 'checkOut'])
pyplot.hist(a, bins, alpha=0.5, label='build')
pyplot.hist(b, bins, alpha=0.5, label='room')
pyplot.hist(c, bins, alpha=0.5, label='checkIn')
pyplot.hist(d, bins, alpha=0.5, label='checkOut')
pyplot.legend(loc='upper right')
pyplot.show()
