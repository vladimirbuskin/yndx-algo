# ID посылки: 68569925
import sys
from typing import List

'''
testcases:
0 1 4 9 0
0 7 9 4 8 20
1 3 2 0 1 3
0 1 0
0 0
0
0 4
1 0
'''

def solution(arr: List[int]) -> List[int]:
  # calc distance: from left to right
  fromZero = 10**9
  for i in range(len(arr)):
    fromZero = 0 if arr[i] == 0 else fromZero + 1
    arr[i] = fromZero

  # calc distance: from right to left
  fromZero = 10**9
  for i in range(len(arr)-1,-1,-1):
    fromZero = 0 if arr[i] == 0 else fromZero + 1
    arr[i] = min(fromZero, arr[i])

  return arr

num = int(input())
arr = map(int, sys.stdin.readline().rstrip().split())

print(*solution(arr))