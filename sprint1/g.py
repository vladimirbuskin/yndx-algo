import sys
from typing import List

'''
== ALGO
# n input dec number
# num - array of strings
if n == 0 return 0
num = []
while n > 0:
  num.append(n & 1)
  n >> 1

num.reverse()
return "".join(num)

'''

def solution(n: int) -> str:
  if n == 0: return "0"
  num = []
  while n > 0:
    num.append(str(n & 1))
    n = n >> 1

  num.reverse()
  return "".join(num)

n = int(sys.stdin.readline().rstrip())
print(solution(n))