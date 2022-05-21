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


def find (ar):
  res = "None"
  for i in range(len(ar)-1):
    for j in range(i+1, len(ar)):
      if ar[i] + ar[j] == k:
        return "%s %s" % (ar[i], ar[j])
  return res  


print(find(ar))
