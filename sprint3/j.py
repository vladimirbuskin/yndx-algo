import sys

'''
5
4 3 9 2 1

3 4 2 1 9
3 2 1 4 9
2 1 3 4 9
1 2 3 4 9
'''

def sort(ar):
  printed = False
  sorted = False
  while not sorted:
    sorted = True
    for i in range(len(ar)-1):
      if ar[i] > ar[i+1]:
        ar[i], ar[i+1] = ar[i+1], ar[i]
        sorted = False
    if not sorted:
      print(" ".join(map(str,ar)))
      printed = True
  if not printed:
    print(" ".join(map(str,ar)))

n = int(input())
ar = [int(c) for c in sys.stdin.readline().split()]
sort(ar)