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
  # color white
  # colors[v1] = 0
  # colors[v2] = 0

def solution(n,adList):
  res = []
  color = {}
  for i in range(n-1,-1,-1):
    dfs(adList, i+1, color, res)
  res.reverse()
  print(*res)
  # for i in range(len(res)-1,-1,-1):
  #   r = res[i]
  #   print(r," ",end="")

def dfs(adList, s, color, res):
  st = [s]
  while len(st) > 0:
    v = st.pop()
    #print('====', v)

    # white color
    if color.get(v, 0) == 0:
      # color grey and add back
      color[v] = 1
      st.append(v)

      # process white neighbors
      nbrs = adList.get(v, [])
      for n in nbrs:
        # we add white
        if color.get(n, 0) == 0:
          st.append(n)

    # grey, we are going back
    elif color.get(v, 0) == 1:
      color[v] = 2
      # on way back we add vertex to result
      res.append(v)


solution(n, adList)