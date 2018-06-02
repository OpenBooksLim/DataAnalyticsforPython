# -*- coding: utf-8 -*-
# filename : pandas_ex.py
# Step 1. pandas, numpy를 import합니다.
import pandas as pd
import numpy as np

# Series 생성
s = pd.Series([1, 2, 3, 4, 5, np.nan])
print(s)
print('-----')

dates = pd.date_range('20180511', periods=10)
print(dates)
print('-----')

# dates 인덱스로 생성, row x col(A, B, C, D)
df = pd.DataFrame(np.random.rand(10, 4), index=dates, columns=list('ABCD'))
print(df)
print('-----')

print(df.head(3))
print(df.tail(2))
print(df.index)
print(df.columns)
print(df.values)
print('-----')

print(df.describe())
print(df.T)
print('-----')

print(df.sort_index(axis=0, ascending=False))
print(df.sort_values(by='B'))
print('-----')

# Getting
print(df['C'])
print(df[1:3])
print(df.loc[:, ['A', 'B']])
print(df.loc[:'20180513'], ['C', 'D'])
print(df.loc[dates[1], 'C'])
print('-----')

# Boolean indexing
print(df.A > 0)
print(df[df > 1])
print(df > 0)
print('-----')

# Operation
print(df.mean(0))
print(df.mean(1))
print('-----')

# Merge
df = pd.DataFrame(np.random.rand(10, 5))
print(df)
pieces = [df[:2], df[4:6], df[8:]]
print(pd.concat(pieces))
print('-----')

# Join
left = pd.DataFrame({'key' : ['A', 'B', 'C', 'C'], 'lval' : [1, 2, 3, 4]})
print(left)
right = pd.DataFrame({'key' : ['A', 'B', 'C'], 'rval' : [5, 6, 7]})
print(right)
print(pd.merge(left, right, on='key'))
