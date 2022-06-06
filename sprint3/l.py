import sys
#import bisect

def bisectLeft(ar, x, left, right):
  # exit
  if left >= right:
    return left

  # med
  med = (left + right) // 2
  #print("left=%s med=%s right=%s" % (left, med, right))

  # found
  if ar[med] == x:
    return bisectLeft(ar, x, left, med)
  # [left, med)
  elif x < ar[med]:
    return bisectLeft(ar, x, left, med)
  # [med, right)
  else:
    return bisectLeft(ar, x, med+1, right)

# print(10 + 5 // 2)

def findDay(ar, x):
  i = bisectLeft(ar, x, 0, len(ar))
  #i = bisect.bisect_left(ar, x, 0, len(ar))
  # found a day
  # [2,3,4] x=5 => -1
  if i == len(ar):
    return -1
  # [2,4,5] x=3 => i + 1
  # [2,4,5] x=4 => i + 1
  else:
    return i + 1

def solution(ar, x):
  i1 = findDay(ar, x)
  i2 = findDay(ar, x * 2)
  print("%s %s" % (i1, i2))

n = input()
ar = [int(x) for x in sys.stdin.readline().split()]
x = int(input())

solution(ar, x)

