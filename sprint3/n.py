import sys
import functools
from typing import List

'''
4
7 8
7 8
2 3
6 10

'''

def solution(ar: List[str]) -> List[str]:
  '''
  take first
  take next, if they can be joined join, and keep in current
  if cant be joined push to out array, take new array as current

  [1,1], [1,2]

  [1,10], [2,3]
  '''
  ar.sort()

  if len(ar) == 0:
    return
  
  cur = ar[0]
  for i in range(1, len(ar)):
    if cur[1] >= ar[i][0]:
      cur = [cur[0], max(cur[1], ar[i][1])]
    else:
      print(" ".join(map(str,cur)))
      cur = ar[i]
  print(" ".join(map(str,cur)))


n = int(input())
ar = []
for i in range(n):
  ar.append([int(x) for x in sys.stdin.readline().split()])

solution(ar)