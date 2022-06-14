import sys

'''
[2 3 4 0 1]

'''

def find_shift(ar, l, r):
  if r - l <= 1:
    return (l + 1) % len(ar)
  m = (l + r) // 2
  if ar[l] > ar[m]:
    return find_shift(ar, l, m)
  else:
    return find_shift(ar, m, r)

def bisect_left(nums, l, r, target, shift):
  sl = (l + shift) % len(nums)

  if r - l <= 1:
    if nums[sl] == target:
      return sl
    else:
      return -1

  m = (l + r) // 2
  sm = (m + shift) % len(nums)

  # found
  if target == nums[sm]:
    return sm
  # [l, m)
  elif target < nums[sm]:
    return bisect_left(nums, l, m, target, shift)
  # [m, r)
  else:
    return bisect_left(nums, m + 1, r, target, shift)

def broken_search(nums, target) -> int:
  shift = find_shift(nums, 0, len(nums))
  return bisect_left(nums, 0, len(nums), target, shift)

# def test():
#     arr = [19, 21, 100, 101, 1, 4, 5, 7, 12]
#     print(broken_search(arr, 1))

# n = int(input())
# target = int(input())
# nums = [int(i) for i in input().split(" ")]
# print(broken_search(nums, target))

