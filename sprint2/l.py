import sys

def fibonachi(n, k):

  if n == 0 or n == 1:
    return 1

  max = 10**k
  p1 = 1
  p2 = 1
  while n > 1:
    r = (p1 + p2) % max
    p1 = p2
    p2 = r
    n -= 1
  
  return p2

n, k = map(int, input().split())
print(fibonachi(n, k))