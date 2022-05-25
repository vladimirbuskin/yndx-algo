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
  # init distance array
  dist = [10**9] * len(arr)

  # calc distance: from left to right
  fromZero = 10**9
  for i in range(len(arr)):
    fromZero = 0 if arr[i] == 0 else fromZero + 1
    dist[i] = min(fromZero, dist[i])

  # calc distance: from right to left
  fromZero = 10**9
  for i in range(len(arr)-1,-1,-1):
    fromZero = 0 if arr[i] == 0 else fromZero + 1
    dist[i] = min(fromZero, dist[i])

  return dist

num = int(input())
arr = [ int(x) for x in sys.stdin.readline().rstrip().split(" ")]

print(" ".join(map(str, solution(arr))))