import sys
from typing import List


def solution(k: int, arr: List[int]) -> int:
  points = 0
  # I think we can limit this array to [min..max] iterations, where min and max
  # minimum and maximum values found in arr, but that doesn't change worst case time complexity
  # when min=1 and max=9
  for round in range(1,10):
    if (arr[round] > 0):
      points += arr[round] <= k * 2
  return points

k = int(input())

# array will contain count of digits
# if 2 is 4 times in input matrix arr[2] == 4
# if 9 is not in input matrix arr[9] == 0
arr = [0]*10
for i in range(0, 4):
  str = input()
  for j in range(0, 4):
    ch = str[j]
    if ch != '.':
      arr[int(ch)] += 1

print(solution(k, arr))