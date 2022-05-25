# ID посылки: 68593725
import sys
from typing import List

def solution(k: int, arr: List[int]) -> int:
  return sum(0 < p <= k * 2 for p in arr)

k = int(input())

# array will contain count of digits
# if 2 is 4 times in input matrix arr[2] == 4
# if 9 is not in input matrix arr[9] == 0
arr = [0]*10
for i in range(4):
  str = input()
  for j in range(4):
    ch = str[j]
    if ch != '.':
      arr[int(ch)] += 1

print(solution(k, arr))