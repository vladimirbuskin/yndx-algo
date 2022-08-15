#from collections import deque
n, m = [int(x) for x in input().split()]

adList = {}
colors = {}
for i in range(m):
  v1, v2 = [int(x) for x in input().split()]
  # init
  if adList.get(v1) == None: adList[v1] = []
  if adList.get(v2) == None: adList[v2] = []
  adList[v1].append(v2)
  adList[v2].append(v1)
  # color white
  # colors[v1] = 0
  # colors[v2] = 0

def dfs(adList, v, colors):
  comp = set()
  if colors.get(v, 0) != 0:
    return []

  # make iterative DFS
  st = [v]
  while len(st) > 0:
    v = st.pop()
    # color it and add into components
    colors[v] = 1
    comp.add(v)
    # get linked nodes
    nodes = adList.get(v, [])
    for n in nodes:
      # if not visited yet we add to stack
      if colors.get(n, 0) == 0:
        st.append(n)
  return list(comp)

def solution(n, adList, colors):
  comps = [];
  
  # iterate all vertexes
  for v in range(1, n+1, 1):
    comp = dfs(adList, v, colors)
    if len(comp)>0:
      comp.sort()
      comps.append(comp)

  # sort in proper order
  comps.sort()

  # out
  print(len(comps))
  for comp in comps:
    print(*comp)

solution(n, adList, colors)