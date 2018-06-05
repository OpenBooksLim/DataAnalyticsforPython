# Step 1. 필요한 모듈을 import합니다.
# -*- coding: utf-8 -*-
import common.common as cm
import pprint as pp
import statistics as st
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
    params = 'serviceKey=%s&HOUR=24&COURSE_ID=1&pageNo=1&startPage=1&numOfRows=999&pageSize=999&CURRENT_DATE=%s' % (cm.get_serviceKey(), current_date)
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
# Step 4-1. statistics를 활용한 통계량 분석
fdIndex.sort()
# ts = map(float, fdIndex)
try:
    print('mean:::', st.mean(map(float, fdIndex)))
    print('harmonic_mean:::', st.harmonic_mean(map(float, fdIndex)))
    print('median:::', st.median(map(float, fdIndex)))
    print('median_low:::', st.median_low(map(float, fdIndex)))
    print('median_high:::', st.median_high(map(float, fdIndex)))
    print('median_grouped:::', st.median_grouped(map(float, fdIndex)))
    print('pstdev:::', st.pstdev(map(float, fdIndex)))
    print('stdev:::', st.stdev(map(float, fdIndex)))
    print('pvariance:::', st.pvariance(map(float, fdIndex)))
    print('variance:::', st.variance(map(float, fdIndex)))
except Exception as e:
    print(str(e))

# 45행의 ts를 사용할 경우 에러 발생에 대한 시험 코드
'''try:
    print('mean:::', st.mean(ts))
    print('harmonic_mean:::', st.harmonic_mean(ts))
    print('median:::', st.median(ts))
    print('median_low:::', st.median_low(ts))
    print('median_high:::', st.median_high(ts))
    print('median_grouped:::', st.median_grouped(ts))
    print('pstdev:::', st.pstdev(ts))
    print('stdev:::', st.stdev(ts))
    print('pvariance:::', st.pvariance(ts))
    print('variance:::', st.variance(ts))
except Exception as e:
    print(str(e))'''

# Step 5. 분석을 위한 표본에 대하여 시각화를 진행합니다.
plt.hist(fdIndex)
plt.title("식중독지수 히스토그램(Histogram)")
plt.xlabel("값(Value)")
plt.ylabel("빈도(Frequency)")
plt.show()
