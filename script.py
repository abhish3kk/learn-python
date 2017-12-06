#!/usr/bin/python3.5m

import sys

def solve(a0, a1, a2, b0, b1, b2):
    # Complete this function
    sumA = 0
    sumB = 0
    arr = [a0, a1, a2]
    brr = [b0, b1, b2]
    for x in range(len(arr)):
      if arr[x] > brr[x]:
        sumA += 1
      elif arr[x] < brr[x]:
        sumB += 1
      else:
        sumA += 0
        sumB += 0

    return "%s%s"% (sumA, sumB)


a0, a1, a2 = input().strip().split(' ')
a0, a1, a2 = [int(a0), int(a1), int(a2)]
b0, b1, b2 = input().strip().split(' ')
b0, b1, b2 = [int(b0), int(b1), int(b2)]
result = solve(a0, a1, a2, b0, b1, b2)
print (" ".join(map(str, result)))