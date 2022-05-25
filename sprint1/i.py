import sys
from typing import List

'''
== ALGO

cur = 4
while cur < num:
  cur *= 4
return cur == num

'''

def solution(num):
  cur = 1
  while cur<num:
    cur *= 4
  return num == cur

num = int(input())
print(solution(num))