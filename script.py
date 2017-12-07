#!/usr/bin/python3.5m

import sys

n = int(input().strip())
a = []
for a_i in range(n):
    a_t = [int(a_temp) for a_temp in input().strip().split(' ')]
    a.append(a_t)
sum1 = 0
sum2 = 0
for i in range(n):
  for j in range(n):
    if i==j:
      sum1+=a[i][j]
    if j==((n-1)-i):
      sum2+=a[i][j]
res = sum1-sum2
if res<0:
  res = res * -1
print(res)