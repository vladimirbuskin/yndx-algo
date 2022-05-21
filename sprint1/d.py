from calendar import c
import sys
from typing import List

def solution(list: List[int]) -> int:
  count = 0
  for i in range(len(list)):
    if (
      # check on left
      (i - 1 < 0 or list[i-1] < list[i]) and
      # check on right
      (i + 1 >= len(list) or list[i] > list[i+1])
    ):
      count += 1

  return count

n = int(input())
list = [int(x) for x in input().split(" ")]

print(solution(list))
