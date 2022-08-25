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
  colors[v1] = 0
  colors[v2] = 0

s = int(input())

def solution(adList, colors):
  print(adList)

solution(adList, colors)