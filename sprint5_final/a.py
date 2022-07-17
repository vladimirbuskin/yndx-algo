# посылка 69284162
import sys

'''
-- ПРИНЦИП РАБОТЫ --

-- ВРЕМЕННАЯ СЛОЖНОСТЬ --

-- ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ --

где:
N - кол-во слов в одной поисковой фразе
D - кол-во документов

       1          i = 1
     /   \
    2      3      i = 2 3
   / \    /  \
  8   6   4   7   i = 4 5 6 7

'''


class MinHeap:

  def __init__(self, comparator):
    self.ar = [0]
    self.comparator = comparator

  def getParentIndex(self, i):
    return i // 2

  def getChildRightIndex(self, i):
    return i * 2 + 1

  def getChildLeftIndex(self, i):
    return i * 2

  def add(self, value):
    self.ar.append(value)
    # index of element is equal to len, because first element is not used
    self.siftUp(len(self.ar)-1)

  def pop(self):
    # there is no more elements left
    if len(self.ar) <= 1:
      return None
    # return value
    result = self.ar[1]
    last = self.ar.pop()
    if len(self.ar) > 1:
      self.ar[1] = last
      # sift down
      self.siftDown(1)
    
    return result

  def siftDown(self, ind):
    '''
    1
  2
len = 3
i = 1
li = 2
ri = 3

    '''
    # find children indexes
    li = self.getChildLeftIndex(ind)
    ri = self.getChildRightIndex(ind)
    ci = None

    # base case, index out of array length
    if (li > len(self.ar)-1):
      return
    
    # if there is no right node, take left node
    if ri > len(self.ar)-1:
      ci = li
    # we take smallest value
    elif self.comparator(self.ar[li]) <= self.comparator(self.ar[ri]):
      ci = li
    else:
      ci = ri

    # if parent node still smaller than smallest child, we switch and recurse lower
    #print('COMPARE', self.ar, ind, ci)
    if self.comparator(self.ar[ind]) > self.comparator(self.ar[ci]):
      self.ar[ind], self.ar[ci] = self.ar[ci], self.ar[ind]
      self.siftDown(ci)

  def siftUp(self, ind):
    if (ind <= 1):
      return 
    # if parent is smaller, we switch
    parInd = self.getParentIndex(ind)
    if self.comparator(self.ar[parInd]) > self.comparator(self.ar[ind]):
      # switch
      self.ar[parInd], self.ar[ind] = self.ar[ind], self.ar[parInd]
      self.siftUp(parInd)

heap = MinHeap(lambda x: x)

# get docs
n = int(input())
for i in range(n):
  [ name, solved, fine ] = input().split(" ")
  # sort: biggest solved, smallest fine, name
  node = [-int(solved), int(fine), name]
  heap.add(node)

n = heap.pop()
while n != None:
  print(n[2]);

  n = heap.pop();
