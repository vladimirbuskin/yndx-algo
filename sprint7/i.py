#from collections import deque
n, m = map(int, input().split())

ar = []
d = []
for i in range(n):
  ar.append(input())
  d.append([0]*m)

for r in range(n-1,-1,-1): # 1,0
  for c in range(0, m):
    bot = d[r+1][c] if r+1 < n else 0
    lft = d[r][c-1] if c-1 >= 0 else 0

    d[r][c] = max(bot,lft) + (1 if ar[r][c]=='1' else 0)

path = []

r = 0
c = m-1


while (r < n-1 or c > 0):

  if r == n-1:
    c-=1
    path.append("R")
    # print('finish R', r, c)
    continue

  if c == 0:
    r+=1
    path.append("U")
    # print('finish U')
    continue

  bot = d[r+1][c]
  lft = d[r][c-1]
  if lft >= bot:
    path.append("R")
    c-=1
    # print('move R')
  else:
    path.append("U")
    r+=1
    # print('move U')

print(d[0][m-1])
path.reverse()
print("".join(path))


# print(ar)
# print(d)