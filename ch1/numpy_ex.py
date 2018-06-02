# -*- coding: utf-8 -*-
# filename : numpy_ex.py
# Step 1. numpy를 import합니다.
import numpy as np

# Step 2. Ex1. 배열 생성 및 수정
a = np.array([1, 2, 3])
print(type(a))
print(a.shape)
print(a[0], a[1], a[2])
a[0] = 4
print(a)

b = np.array([[1, 2, 3],[4, 5, 6]])
print(b.shape)
print(b[0, 0], b[1, 0])
b[0, 0] = 7
print(b)

# Step 3. Ex2. 배열연산
a = np.array([[1, 2], [3, 4]], dtype=np.float64)
b = np.array([[5,6 ], [7, 8]], dtype=np.float64)

print(a + b)
print(np.add(a, b))

print(a - b)
print(np.subtract(a, b))

print(a * b)
print(np.multiply(a, b))

print(a / b)
print(np.divide(a, b))

print(np.sqrt(a))

# Step 4. Ex3. 브로드캐스팅
# 차원이 다른 배열의 계산 : 브로드캐스팅 전
a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
b = np.array([1, 0, 1])
c = np.empty_like(a)

for i in range(4):
    c[i, :] = a[i, :] + b
print(c)

# 브로드캐스팅 적용 후
a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
b = np.array([1, 0, 1])
c = a + b
print(c)
