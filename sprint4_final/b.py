import sys
import math
import time

'''
max number of elements: 10^5 - 100,000
коэф наполнения 1/3 - 2/3
1/4 - 10^5 * 4 => 400,000  Prime number in that range 400009


2*2*2*2 => 2^4 => 4^2
2*2*2 => 2^3
2*2 => 2^2
'''

ALPHA = 2 / (1 + pow(5, 0.5))

 
class MyHashTable:

  C1 = 2
  C2 = 3

  EMPTY = -1
  DELETED = -2

  def __init__(self):
    self.M = 400009
    #self.M = 97
    # we store, [<key>,<value>]
    self.table = [[self.EMPTY, None] for _ in range(self.M)]
  
  # returns number in [0..1) interval
  def __hash(self, n):
    global ALPHA
    return (n * ALPHA) % 1

  # returns key in [0..M) interval
  def __key(self, n):
    return math.floor(self.__hash(n) * self.M)

  # get next address to put collision values
  def __probeSquareNext(self, ki, i):
    ki = (ki + self.C1*i + self.C2*i*i) % self.M
    return ki

  def put(self, key:int, value:int):
    # key index
    ki = self.__key(key)
    i = 1
    # we skip non-empty values with different keys
    # print('ki', ki, self.table[ki])
    while (self.table[ki][0] > self.EMPTY) and (self.table[ki][0] != key):
      ki = self.__probeSquareNext(ki, i)
      # print('ki', ki, self.table)
      # print('probe',key, '=', value, 'ki =',ki,self.table[ki][0])
      i += 1

    # option 1: cell is empty
    # option 2: cell has current key
    self.table[ki][0] = key   # in both cases we update key, it doesn't hurt
    self.table[ki][1] = value # we set value

  def get(self, key:int):
    # key index
    ki = self.__key(key)
    i = 1
    # we skip DELETED and non-empty values with different keys
    while self.table[ki][0] == self.DELETED or ((self.table[ki][0] > self.EMPTY) and (self.table[ki][0] != key)):
      ki = self.__probeSquareNext(ki, i)
      i += 1
    # we found proper key
    if self.table[ki][0] == key:
      return self.table[ki][1]
    # we got till empty cell
    return None

  def delete(self, key:int):
    # key index
    ki = self.__key(key)
    i = 1
    # we skip DELETED and non-empty values with different keys
    while self.table[ki][0] == self.DELETED or ((self.table[ki][0] > self.EMPTY) and (self.table[ki][0] != key)):
      ki = self.__probeSquareNext(ki, i)
      i += 1
    # we found proper key
    if self.table[ki][0] == key:
      self.table[ki][0] = self.DELETED
      return self.table[ki][1]
    return None

class HashTable:

  def __init__(self):
    self.table = {}
  
  def put(self, key:int, value:int):
    self.table[key] = value

  def get(self, key:int):
    return self.table.get(key)

  def delete(self, key:int):
    ret = None
    if key in self.table:
      ret = self.table[key]
      del self.table[key]
    return ret

ht = MyHashTable()

n = int(input())
ar = []
for i in range(n):
  ln = input().split()
  if ln[0] == 'get':
    print(ht.get(int(ln[1])))
  if ln[0] == 'put':
    ht.put(int(ln[1]),int(ln[2]))
  if ln[0] == 'delete':
    print(ht.delete(int(ln[1])))
