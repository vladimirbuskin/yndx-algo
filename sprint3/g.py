import sys


'''
  0 2 1 2 0 0 1
  l
              r
    c
'''

def solution(ar):
  l = -1
  r = len(ar)
  c = 0

  while c < r:
    if ar[c] == '0':
      l += 1
      if c <= l:
        c = l + 1
      if ar[l] == '0':
        continue
      # swap l and c elements
      ar[l],ar[c] = ar[c],ar[l]
    elif ar[c] == '2':
      r -= 1
      if ar[r] == '2':
        continue
      # swap r and c elements
      ar[r],ar[c] = ar[c],ar[r]
    else:
      c += 1

  return ar

n = int(input())
ar = [x for x in sys.stdin.readline().split()]
print(" ".join(solution(ar)))
