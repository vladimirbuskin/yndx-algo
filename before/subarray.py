_data = """6
1 2 3 4 1 2 5 4
2"""

#1 2 3 4 1 2 5 4

inputo = input

def input():
  global _data
  if type(_data) is str:
    _data = _data.split("\n")
  return _data.pop(0)

# =================================================

n = int(input())
ar = list(map(lambda x: int(x), input().split()))
k = int(input())


# def find (ar):
#   set = {}
#   i = 0
#   cnt = 0
#   mx = 0
#   while i < len(ar):
#     print(i)
#     print(set)
#     #inputo()
#     if ar[i] not in set:
#       set[ar[i]] = i
#       i += 1
#       cnt +=1
#       mx = max(mx, cnt)
#     else:
#       pi = set[ar[i]]
#       mx = max(mx, i - pi)
#       i = pi + 1
#       set = {}
#       cnt = 0
#   return mx

def find(ar):
  set = {}
  prev = -1
  mx = 0
  for i in range(len(ar)):
    prev = max(prev, set.get(ar[i], -1))
    mx = max(mx, i - prev)
    set[ar[i]] = i

  return mx

print(find(ar))

