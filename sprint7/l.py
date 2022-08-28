#from collections import deque
import sys
n, m = [int(x) for x in input().split()]

# weight = [int(x) for x in input().split()]
line = sys.stdin.readline().rstrip()
weight = [int(x) for x in line.split()]
# weight = weight[0:n]

d = []
d.append([0]*(m+1))
d.append([0]*(m+1))

weight.sort(reverse=True)



for i in range(1, n+1):
  w = weight[i-1]
  ic = i%2
  ip = (i-1)%2
  
  dp = d[ip]
  dc = d[ic]
  for j in range(w, m+1):
    t = dp[j]
    c = w + dp[j - w]
    dc[j] = c if c > t else t

# def pr(d):
#   for i in range(len(d)):
#     print(*d[i])

print(d[n%2][m])
