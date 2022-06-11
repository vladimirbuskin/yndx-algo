import sys


'''
  0 2 1 2 0 0 1
  l
              r
    c
'''

def solution(children, cookies):
  children.sort()
  cookies.sort()
  s = 0;
  while i<len(children) and j<len(cookies):
    if children[i] <= cookies[j]:
      s += 1
      i += 1
      j += 1  
    else:
      j += 1
  return 

n = int(input())
children = [int(x) for x in sys.stdin.readline().split()]
m = int(input())
cookies = [int(x) for x in sys.stdin.readline().split()]

print(solution(children, cookies))
