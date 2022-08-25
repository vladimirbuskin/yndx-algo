#from collections import deque
n, m = map(int, input().split())

ar = []
d = []
for i in range(n):
  ar.append(input())
  d.append([0]*m)

for r in range(n-1,-1,-1): # 1,0
  for c in range(0, m):
    lft = 0
    bot = 0
    if r+1 < n:
      bot = d[r+1][c]
    if c-1 >= 0:
      lft = d[r][c-1]

    d[r][c] = max(bot,lft) + (1 if ar[r][c]=='1' else 0)

print(d[0][m-1])

# print(ar)
# print(d)