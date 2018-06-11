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

# Step 2. 경마정보조회를 위한 요청변수 및 요청주소 등을 구성합니다.
url = 'http://data.kra.co.kr/publicdata/service/hrReg/getHrReg' # 등록마 조회

c = []
params = 'serviceKey=%s' % cm.get_serviceKey()
print('params : ', params)
# 저장을 원할 경우, 화일명을 정의한다.
fn = os.getcwd() + '/data/' + '4-2.da'
# 서비스 호출
_c = cm.call_serviceF(url, params, 'Y', fn)
c.append(_c)
print(c)

# Step 3. item의 구조를 분석하고, 분석하고자 하는 값들을 추출하기 위한 데이터를 전처리합니다.
pp = pp.PrettyPrinter(indent=4)
data = []
for i in range(0, len(c)):
    try:
        # 응답값이 XML일 경우
        _djson = cm.x2j(c[i])
        item = _djson['response']['body']['items']['item']

        pp.pprint(item)
        if (isinstance(item, dict)):
            data.append(item)
        else:
            data.extend(item)
    except Exception as e:
        continue

pp.pprint(data)

# color : 경주마 털색, sex : 경주마 성별
stat = np.empty((0, 2), str)
i = 0
for v in data:
    i += 1
    stat = np.vstack([stat, np.array([v['color'], v['sex']])])
print('stat::: ', stat)
print('color::: ', stat[:, 0])
print('sex::: ', stat[:, 1])

color_counts, sex_counts = clt.Counter(stat[:, 0]), clt.Counter(stat[:, 1])
print(color_counts, sex_counts)

# Step 4. 데이터 분석을 위한 표본에 대하여 시각화를 진행합니다.
x1 = color_counts.keys()
x2 = sex_counts.keys()
y1 = color_counts.values()
y2 = sex_counts.values()

fig, (ax1, ax2) = plt.subplots(2, sharey=True)
ax1.plot(x1, y1, 'ko-')
ax1.set(title='등록마 조회 서비스', ylabel='경주마 털색')
ax2.plot(x2, y2, 'r.-')
ax2.set(xlabel='Counts', ylabel='경주마 성별')

plt.show()

# Step 5. 확률을 계산합니다.
# Step 5-1. 등록마(모수전체) 중 털색이 ['갈색', '밤색', '흑갈색', '회색']인 말을 선택할 확률을 구합니다.
number_of_total_event_occurs = len(data)
print('전체 : %d' %  number_of_total_event_occurs)
color = list(color_counts.keys()) # ['갈색', '밤색', '흑갈색', '회색']
print(color)
i = 0
cp = np.empty((0, 3), str)
for key, value in color_counts.items():
    i += 1
    tv = (value / number_of_total_event_occurs) # probability of color
    cp = np.vstack([cp, np.array([key, value, tv])])
    print('전체(%d)에서 경주마의 털색이 \'%s\'을(를) 뽑을 확률은 %1.2f입니다.' % (number_of_total_event_occurs, key, tv))

print(cp)

# Step 5-2. 등록마(모수전체) 중 성별이 ['암', '수', '거']인 말을 선택할 확률을 구합니다.
sex = list(sex_counts.keys()) # ['암', '수', '거']
print(sex)
i = 0
sp = np.empty((0, 3), str)
for key, value in sex_counts.items():
    i += 1
    tv = (value / number_of_total_event_occurs) # probability of color
    sp = np.vstack([sp, np.array([key, value, tv])])
    print('전체(%d)에서 경주의 성별이 \'%s\'을(를) 뽑을 확률은 %1.2f입니다.' % (number_of_total_event_occurs, key, tv))

print(sp)

cp = pd.Series([0 for i in range(0, 12)]) # Conditional Probability
for c, s in stat:
    for a in range(0, len(color)):
        for b in range(0, len(sex)):
            if ((c == color[a]) and (s == sex[b])):
                cp[(a * 3) + b] += 1

print(cp, (cp / number_of_total_event_occurs))
