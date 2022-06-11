import sys
import functools
from typing import List

'''
abcd
ahbgdcu
'''

def solution(s1: str, s2: str) -> bool:
  if len(s1)==0:
    return True
  l1 = len(s1)
  k = 0
  for i in range(len(s2)):
    if s2[i]==s1[k]:
      k+=1
      if k == l1:
        return True
  return False

s1 = sys.stdin.readline().rstrip()
s2 = sys.stdin.readline().rstrip()
print(solution(s1, s2))