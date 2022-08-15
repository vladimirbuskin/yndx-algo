from collections import deque
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
  colors[v1] = 0
  colors[v2] = 0

s, t = [int(x) for x in input().split()]

def solution(adList, s, t):
  pathMin = None
  st = deque([[0, s]])
  colors = {}
  while len(st)>0:
    lev, v = st.popleft()

    # we found path 
    if v == t:
      return lev

    # color grey and add back
    colors[v] = 1

    # process neighbors only when not found
    nbrs = adList.get(v, [])
    for n in nbrs:
      # we add white
      if colors.get(n, 0) == 0:
        st.append([lev+1, n])
  
  return -1


print(solution(adList, s, t))