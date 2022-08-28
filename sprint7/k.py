#from collections import deque
import sys
import time
n = int(input())
set1 = [int(x) for x in sys.stdin.readline().rstrip().split()]
m = int(input())
set2 = [int(x) for x in sys.stdin.readline().rstrip().split()]



def pr(d):
  print("    ",end="")
  print(*set2)
  for i in range(len(d)):
    if i > 0:
      print(set1[i-1],"", end="")
    else:
      print("  ", end="")
    print(*d[i])



d = []
for i in range(n+1):
  d.append([0]*(m+1))


# forward
for i in range(1, n+1):
  dc = d[i]
  dp = d[i-1]
  for j in range(1, m+1):
    
    # u = d[i-1][j]
    # l = d[i][j-1]
    if set1[i-1] == set2[j-1]:
      dc[j] = dp[j-1] + 1
    else:
      dc[j] = max(dp[j], dc[j-1])

r1 = []
r2 = []

i = n
j = m

# pr(d)

# pr(d)
# backward
# print(set1)
# print(set2)
while i > 0 and j > 0:
  c = d[i][j]
  u = d[i-1][j]
  l = d[i][j-1]

  # print(i, j, c, u, l)
  # time.sleep(0.1)
  if set1[i-1] == set2[j-1]:
    r1.append(i)
    r2.append(j)
    i-=1
    j-=1
    continue

  if c == u and i >= 1:
    i-=1
    continue

  if c == l and j >= 1:
    j-=1
    continue

r1.reverse()
r2.reverse()

#print(r)
print(len(r1))
print(*r1)
print(*r2)


# print(d[n%2][m])
# pr(d)

