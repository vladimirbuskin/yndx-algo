from typing import List

def solution(nums: List[int]) -> int:
  res = [i%2 for i in nums]
  # when all odd - sum will equal number of nums
  # when all even equal 0
  return sum(res) == len(nums) or sum(res) == 0

nums = [int(c) for c in input().split(" ")]
print("WIN" if solution(nums) else "FAIL")