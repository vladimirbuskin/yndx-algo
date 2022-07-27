
n, m = [int(x) for x in input().split()]

adList = {}
for i in range(m):
  v1, v2 = [int(x) for x in input().split()]
  # init
  if adList.get(v1) == None: adList[v1] = []
  adList[v1].append(v2)

keys = adList.keys()
for i in range(n):
  v = i+1
  # init row
  r = [0]*n
  # set row values for a vertex
  vx = adList.get(v)
  if vx != None:
    for j in range(len(vx)):
      r[vx[j]-1] = 1
  # print row
  print(*r)
