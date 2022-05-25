import sys
from typing import List

'''
== ALGO

2 0 3 8 2 0 4 0 2

zi = 0
while arr[zi] != 0:
  zi+=1
i = zi

while i < len(arr):
  if arr[i] == 0:
    i += 1
    continue
  arr[zi], arr[i] = arr[i], arr[zi]
  zi = i
'''


def solution(arr: List[int]) -> List[int]:
  zi = 0
  while arr[zi] != 0:
    zi += 1
  i = zi

  while i < len(arr):
    if arr[i] == 0:
      i += 1
      continue
    arr[zi], arr[i] = arr[i], arr[zi]
    zi += 1

  return arr

arr = [ int(x) for x in sys.stdin.readline().rstrip().split(" ")]

print(solution(arr))