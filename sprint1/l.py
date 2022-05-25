import sys
from typing import List

'''
== ALGO

'''

def solution(str1, str2):
  d = {}
  for i in range(len(str2)):
    d[str2[i]] = d.get(str2[i], 0) + 1

  for i in range(len(str1)):
    d[str1[i]] = d.get(str1[i], 0) - 1
  
  for k in d:
    if d[k]>0:
      return k
  
  return None

str1 = sys.stdin.readline().rstrip()
str2 = sys.stdin.readline().rstrip()

print(solution(str1, str2))