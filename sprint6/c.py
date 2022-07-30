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
  colors[v1] = 0
  colors[v2] = 0
s = int(input())

'''
0 - white
1 - gray
2 - black
'''

def dfs(adList, s, colors):
  st = []
  st.append(s)
  while len(st) > 0:
    s = st.pop()
    # if not visited continue
    if colors.get(s, 0) == 0:
      # process
      print(s)
      # mark grey
      colors[s] = 1
      # put back
      st.append(s)
      # take white neighbours
      for i in range(len(adList.get(s, []))-1,-1,-1):
        v = adList[s][i]
        # take only white vertexes
        if colors[v] == 0:
          st.append(v)
    # if grey already
    else:
      # processed
      colors[s] = 2

dfs(adList, s, colors)