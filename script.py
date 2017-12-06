#!/usr/bin/python3.5m

import sys

def simpleArraySum(n, ar):
    # Complete this function
    sum = 0
    for x in ar:
      sum = sum + x

    return sum

n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = simpleArraySum(n, ar)
print(result)

