# -*- coding: utf-8 -*-
# filename : scipy_ex.py
# Step 1. scipy, numpy를 import합니다.
from scipy import linalg # Linear Algebra (scipy.linalg)
from scipy import stats # Statistics (scipy.stats)
from scipy.stats import norm
import numpy as np

# Step 2. Finding Inverse
a = np.array([[1, 3, 5], [2, 5, 1], [2, 3, 8]])
print(a)
print(linalg.inv(a))
print(a.dot(linalg.inv(a)))
print('-----')

# Step 3. Solving linear system
a = np.array([[1, 2], [3, 4]])
print(a)
b = np.array([[5], [6]])
print(b)

print(linalg.inv(a).dot(b))
print(a.dot(linalg.inv(a).dot(b)) - b)
print(np.linalg.solve(a, b))
print(a.dot(np.linalg.solve(a, b)) - b)
print('-----')

# Step 4. Common Methods in stats
print(norm.cdf(0))
print(norm.cdf([-1., 0, 1]))
print(norm.cdf(np.array([-1., 0, 1])))
print(norm.mean(), norm.std(), norm.var())
print(norm.stats(moments="mv"))
print(norm.ppf(0.5))
print(norm.rvs(size=3))
print(np.random.seed(1234))
print(norm.rvs(size=5, random_state=1234))
print(norm.rvs(5))
print('-----')

# Step 5. Broadcasting
print(stats.t.isf([0.1, 0.05, 0.01], [[10], [11]]))
print(stats.t.isf([0.1, 0.05, 0.01], 10))
print(stats.t.isf([0.1, 0.05, 0.01], [10, 11, 12]))
print('-----')

# Step 6. Anlysing one sample
np.random.seed(282629734)
x = stats.t.rvs(10, size=1000)

# Descriptive statistics
print(x.min())
print(x.max())
print(x.mean())
print(x.var())

m, v, s, k = stats.t.stats(10, moments='mvsk')
n, (smin, smax), sm, sv, ss, sk = stats.describe(x)
sstr = '%-14s mean = %6.4f, variance = %6.4f, skew = %6.4f, kurtosis = %6.4f'
print(sstr % ('distribution:', m, v, s ,k))
print(sstr % ('sample:', sm, sv, ss, sk))
print('-----')

# T-test
print('t-statistic = %6.3f pvalue = %6.4f' %  stats.ttest_1samp(x, m))
tt = (sm - m) / np.sqrt(sv / float(n))
pval = stats.t.sf(np.abs(tt), n - 1) * 2
print('t-statistic = %6.3f pvalue = %6.4f' % (tt, pval))
print('-----')
