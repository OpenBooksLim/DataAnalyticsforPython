# Step 1. 필요한 모듈을 import합니다.
# -*- coding: utf-8 -*-
import common as cm
import pprint as pp
import scipy as sp
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
rc('font', family=font_name)

# Step 2. 요청변수 및 요청주소 등을 구성합니다.
url = 'http://newsky2.kma.go.kr/service/TourSpotInfoService/SpotIdxData' # 기상지수 예보 조회(A)
qDate = ['20180305', '20180315', '20180321']
c = []
for i in range(0, len(qDate)):
    current_date = qDate[i] + '01'
    params = 'HOUR=24&COURSE_ID=1&pageNo=1&startPage=1&numOfRows=%d&pageSize=%d&CURRENT_DATE=%s' % (999, 999, current_date)
    print('params : ', params)

    # 서비스 호출
    _c = cm.call_service(url, params)
    c.append(_c)
    print(c[i])

# Step 3. item의 구조를 분석하고, 분석하고자 하는 값들을 추출하기 위한 데이터를 전처리합니다.
pp = pp.PrettyPrinter(indent=4)
data = []
for i in range(0, len(c)):
    _djson = cm.x2j(c[i])
    item = _djson['response']['body']['items']['item']
    pp.pprint(item)
    data.extend(item)
pp.pprint(data)

fdIndex = []
i = 0
for v in data:
    i += 1
    fdIndex.append(int(v['fdIndex']))
print('fdIndex::: ', fdIndex)

# Step 4. 데이터(식중독지수) 분석을 수행합니다.
# Step 4-3. SciPy를 활용한 통계량 분석, 해당 library 설명
# fdIndex.sort()
try:
    print('mean : {0:8.6f}'.format(sp.mean(fdIndex)))
    print('average : {0:8.6f}'.format(sp.average(fdIndex)))
    print('median : {0:8.6f}'.format(sp.median(fdIndex)))
    print('std : {0:8.6f}'.format(sp.std(fdIndex)))
    print('var : {0:8.6f}'.format(sp.var(fdIndex)))
except Exception as e:
    print(str(e))

# Step 5. 분석을 위한 표본에 대하여 시각화를 진행합니다.
plt.hist(fdIndex)
plt.title("식중독지수 히스토그램(Histogram)")
plt.xlabel("값(Value)")
plt.ylabel("빈도(Frequency)")
plt.show()