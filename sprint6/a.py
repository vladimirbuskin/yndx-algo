
n, m = [int(x) for x in input().split()]

adList = {}
for i in range(m):
  v1, v2 = [int(x) for x in input().split()]
  # init
  if adList.get(v1) == None: adList[v1] = []
  adList[v1].append(v2)

keys = adList.keys()
for i in range(n):
  # init
  vs = adList.get(i+1)
  if vs == None:
    print(0)
  else:
    print(len(vs), *sorted(vs))
