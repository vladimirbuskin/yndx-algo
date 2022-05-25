_data = """6
-9 -7 -6 -1 -1 3
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
  set = {}
  res = "None"
  for i in range(len(ar)):
    compl = k - ar[i];
    if compl in set:
      return ("%s %s" % (ar[i], compl))
    else:
      set[ar[i]] = i
  return res

print(find(ar))
