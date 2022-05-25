import sys
from typing import List

'''
== ALGO
mx = max(len(num1),len(num2))
out = []
perenos = 0
for i in range(mx)
  d1 = 0
  d2 = 0
  if i < len(num1): d1 = int(num1[len(num1)-i-1])
  if i < len(num2): d2 = int(num2[len(num2)-i-1])
  dc = d1 + d2 + perenos
  out.append(dc & 1)
  perenos = dc >> 1
if perenos==1:
  out.append("1")

'''

def solution(num1: str, num2: str):
  mx = max(len(num1),len(num2))
  out = []
  perenos = 0
  for i in range(mx):
    d1 = 0
    d2 = 0
    if i < len(num1): d1 = int(num1[len(num1)-i-1])
    if i < len(num2): d2 = int(num2[len(num2)-i-1])
    dc = d1 + d2 + perenos
    out.append(str(dc & 1))
    perenos = dc >> 1
  if perenos == 1:
    out.append(str(perenos))
  out.reverse()
  return "".join(out)

num1 = sys.stdin.readline().rstrip()
num2 = sys.stdin.readline().rstrip()

print(solution(num1, num2))