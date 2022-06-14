import sys

'''
pivot = 4
 0 1 2 3 4
[1 6 4 2 3]
'''

class QuickSorter:

  def __partition(self, ar, l, r, key):
    li = l
    ri = r
    pivot = key(ar[l+(r-l)//2])
    while li <= ri:
      if key(ar[li]) < pivot:
        li += 1
        continue
      if key(ar[ri]) > pivot:
        ri -= 1
        continue
      ar[li],ar[ri] = ar[ri],ar[li]
      li += 1
      ri -= 1
    return li

  def __sort(self, ar, l, r, key):
    if r-l <= 0:
      return
    c = self.__partition(ar, l, r, key)
    self.__sort(ar, l, c-1, key)
    self.__sort(ar, c, r, key)
  
  def sort(self, ar, key):
    return self.__sort(ar, 0, len(ar)-1, key)

def solution(ar):
  sorter = QuickSorter()
  
  def sortKey(el):
    return [-el[0],el[1],el[2]]
  
  sorter.sort(ar, sortKey)
  return ar

n = int(input())
ar = []
for i in range(n):
  name, score, fine = input().split()
  ar.append([int(score), int(fine), name])

sorted = solution(ar)
for el in sorted:
  print(el[2])
