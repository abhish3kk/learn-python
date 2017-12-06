#!/usr/bin/python3.5m

import sys

def simpleArraySum(n, ar):
    # Complete this function
    sum = 0
    for x in ar:
      sum = sum + x

    return sum

print("Enter size of array")
n = int(input().strip())
print("Enter elements separated by ' '")
ar = list(map(int, input().strip().split(' ')))
if n != len(ar):
  print("size of array specified doesn't match with length of array. Please enter elements correctly")
ar = list(map(int, input().strip().split(' ')))
result = simpleArraySum(n, ar)
print(result)
