from typing import List

def solution(nums: List[int]) -> int:
  a, x, b, c = nums
  return a * (x ** 2) + b * x + c


nums = [int(c) for c in input().split(" ")]
print(solution(nums))