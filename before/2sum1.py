_data = """6
-1 -1 -9 -7 3 -6
2"""

# _data = """8
# 6 2 8 -3 1 1 6 10
# 100"""

def input():
  global _data
  if type(_data) is str:
    _data = _data.split("\n")
  return _data.pop(0)

# =================================================

n = int(input())
ar = list(map(lambda x: int(x), input().split()))
k = int(input())


def find (ar,k):
  res = "None"
  ar.sort()
  l = 0
  r = len(ar)-1
  while l<r:
    sum = ar[l] + ar[r]
    if sum == k:
      return "%s %s" % (ar[l], ar[r])
    if sum < k:
      l+=1
    if (sum > k):
      r-=1
  return res 

print(find(ar,k))
