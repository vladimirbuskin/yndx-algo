from filecmp import cmp
import sys
import functools
from typing import List

def less(a,b):
  ca = 0
  cb = 0
  for i in range(max(len(a),len(b))):
    # take char by char if equal continue
    if i<len(a):
      ca = int(a[i])
    if i<len(b):
      cb = int(b[i])
    if ca < cb:
      return -1
    elif ca > cb:
      return 1
  return 0

def keyGen(a):
  return a.ljust(4,a[-1])

def solution(ar: List[str]) -> List[str]:
  ar.sort(reverse=True, key=keyGen)
  return ar
  
n = int(input())
ar = sys.stdin.readline().split()
print("".join(solution(ar)))
