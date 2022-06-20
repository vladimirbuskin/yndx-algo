import sys

'''

'''


def solution(nums):
  
  diffDic = {0:0, 1:0}
  diff = [0]*len(nums)

  # find new array of diffs.
  for i in range(len(nums)):
    n = nums[i]
    diffDic[n] += 1
    diff[i] = diffDic[0] - diffDic[1]

  # walk diffs write index of diff when find, and if same diff found, find max between 
  mx = 0
  prev = {0:-1}
  for i in range(len(diff)):
    d = diff[i]
    if prev.get(d) == None:
      prev[d] = i
    else:
      mx = max(mx, i - prev[d])

  return mx

n = int(input())
nums = []
if (n > 0):
  nums = [int(x) for x in input().split(" ")]

print(solution(nums))
