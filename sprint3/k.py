import sys
import functools
from typing import List

'''
abcd
ahbgdcu
'''

def merge(arr: list, left: int, mid: int, right: int) -> list:
  '''
  [1 2 3 4 8 7 6 5]
   l       m 
  while left<mid  && right

  [left,mid)[mid, right)
  '''
  res = []
  l = left
  m = mid
  while l < mid and m < right:
    if arr[l]<=arr[m]:
      res.append(arr[l])
      l+=1
    else:
      res.append(arr[m])
      m+=1
  while l<mid:
    res.append(arr[l])
    l+=1
  while m<right:
    res.append(arr[m])
    m+=1
  return res

def merge_sort(list: list, left: int, right: int) -> None:
  # base case
  if right - left <= 1:
    return
  mid = (right + left) // 2  # 4,5 => 2
  # left side
  merge_sort(list, left, mid)
  # right side
  merge_sort(list, mid, right)
  # merge
  srtd = merge(list, left, mid, right)
  j = 0
  # copy back
  for i in range(left, right):
    list[i] = srtd[j]
    j += 1

def solution(ar: list) -> list:
  merge_sort(ar, 0, len(ar))
  return ar

ar = [3,6,2,1,4,8,7,0]
print(solution(ar))