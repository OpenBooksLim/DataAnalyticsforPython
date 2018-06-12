# Step 1. 필요한 모듈을 import합니다.
# -*- coding: utf-8 -*-
import common.common as cm
import pprint as pp
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
rc('font', family=font_name)
import os
import numpy as np
from datetime import date, timedelta
import collections as clt
import pandas as pd
import random

# Step 2. 경마정보조회를 위한 요청변수 및 요청주소 등을 구성합니다.
# Step 2-1. Looging을 위하여 공통 모듈에서 로거를 정의합니다.
f = cm.pre_logging() # 등록마 조회 결과 파일을 로딩

# Step 2-2. '4-1'에서 저장한 파일을 이용하여 해당 데이터를 로딩합니다.
c = []
fn = os.getcwd() + '/data/' + 'RegisteredHorse.da' # url = 'http://data.kra.co.kr/publicdata/service/hrReg/getHrReg' # 등록마 조회
c.append(cm.open_file(fn, True))
cm.logF(f, c)

# Step 3. item의 구조를 분석하고, 분석하고자 하는 값들을 추출하기 위한 데이터를 전처리합니다.
pp = pp.PrettyPrinter(indent=4)
data = []
for i in range(0, len(c)):
    try:
        # 응답값이 XML일 경우
        _djson = cm.x2j(c[i])
        item = _djson['response']['body']['items']['item']

        # pp.pprint(item)
        if (isinstance(item, dict)):
            data.append(item)
        else:
            data.extend(item)
    except Exception as e:
        continue

# pp.pprint(data)
cm.logF(f, data)

# Step 3-1. data에서 일부 데이터(전체 갯수의 10%수준)를 추출합니다.
data = random.sample(data, int(len(data) * 0.1))
# pp.pprint(data)
cm.logF(f, data)
np.random.shuffle(data)

# Step 3-2. 일부 데이터를 기준으로 각 요소의 빈도를 집계합니다.
# color : 경주마 털색, sex : 경주마 성별
df = pd.DataFrame(data)
cm.logF(f, df)

color_counts = clt.Counter(df['color'])
'''stat = pd.DataFrame(
    np.vstack(np.array(list(color_counts.keys()))), columns=['color']
)
stat['count'] = pd.Series(np.array(list(color_counts.values())))
stat['point'] = pd.Series([10, 5, 3, 2])'''
stat = pd.DataFrame(
    {'color' : list(color_counts.keys()), 'count' : list(color_counts.values()), 'point' : [10, 5, 3, 2]}
)
cm.logF(f, stat)

# Step 4. 확률을 계산합니다. 확률변수 - 기대값, 분산(표준편차)
# Step 4-1. 등록마(표본전체) 중 털색이 ['갈색', '밤색', '흑갈색', '회색']인 말을 선택할 확률을 구합니다.
# 1. 경주마 털색, 2. 뽑을 때 점수, 3. 확률 : ['갈색', '밤색', '흑갈색', '회색'], [10, 5, 3, 2], [ ]
number_of_total_event_occurs = len(data)
cm.logF(f, '***** 확률을 계산합니다. *****')
cm.logF(f, ('표본갯수 : %d' %  number_of_total_event_occurs))
color = list(color_counts.keys()) # ['갈색', '밤색', '흑갈색', '회색']
cm.logF(f, ('경주마 털색 종류 : %s' % color))

i = 0
cp = {}
for key, value in color_counts.items():
    i += 1
    tv = float(value / number_of_total_event_occurs) # probability of color
    cp.update({key : tv})

df_color = pd.DataFrame(
    {'color' : list(cp.keys()), 'probability' : list(cp.values())}
)
cm.logF(f, df_color)

stat = pd.merge(stat, df_color, left_on='color', right_on='color')
cm.logF(f, stat)

# 기대값 : 각 요소별 '확률*포인트(사건이 발생할 때의 결과=이득)'의 합
expectation = (stat['point'] * stat['probability']).sum()
cm.logF(f, '경주마 털색 추출에 대한 기대값은? %f' % expectation)

# 분산 : 기대값과 확률변수들간의 거리(떨어진 정도)
variance = np.var(stat['point'] - expectation)
# 표준편차 : 기대값으로부터의 일반적 차이
stdev = np.std(stat['point'] - expectation)
cm.logF(f, '분산 : %f, 표준편차 : %f' % (variance, stdev))

# Step 5. 데이터 분석을 위한 표본에 대하여 시각화를 진행합니다.
x1 = stat['color']
y1 = stat['count']
x2 = ['기대값', '분산', '표준편차']
y2 = [expectation, variance, stdev]

fig, (ax1, ax2) = plt.subplots(2)
ax1.plot(x1, y1, 'ko-')
ax1.set(title='등록마 조회 서비스', ylabel='경주마 털색')
ax2.plot(x2, y2, 'r.-')
ax2.set(xlabel='%', ylabel='기대값,분산,표준편차')

plt.show()
