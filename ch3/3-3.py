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

# Step 2. 버스위치정보조회를 위한 요청변수 및 요청주소 등을 구성합니다.
url = 'http://ws.bus.go.kr/api/rest/buspos/getBusPosByVehId' # 특정 차량 위치정보 항목조회(vehId)

vehId = ['111033527', '111033034', '111033401', '111033058']
c = []
for i in range(0, len(vehId)):
    params = 'serviceKey=%s&vehId=%s' % (cm.get_serviceKey(), vehId[i])
    print('params : ', params)

    # 저장을 원할 경우, 화일명을 정의한다.
    fn = os.getcwd() + '/data/' + '3-3_%s.da' % str(vehId[i])
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
        item = _djson['ServiceResult']['msgBody']['itemList']

        pp.pprint(item)
        if (isinstance(item, dict)):
            data.append(item)
        else:
            data.extend(item)
    except Exception as e:
        continue

pp.pprint(data)

stat = np.empty((0, 2), int)
i = 0
for v in data:
    i += 1
    stat = np.vstack([stat, np.array([int(v['stopFlag']), int(v['busType'])])])
print('stat::: ', stat)
print('stopFlag::: ', stat[:, 0])
print('busType::: ', stat[:, 1])

# Step 4. 데이터 분석을 위한 표본에 대하여 시각화를 진행합니다.
a = np.trim_zeros(stat[:, 0])
b = np.trim_zeros(stat[:, 1])

bins = np.linspace(-0.5, 1.5, 10)

plt.style.use('seaborn-deep')
plt.hist([a, b], bins, label=['stopFlag', 'busType'])
plt.legend(loc='upper right')
plt.show()
