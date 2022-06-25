import sys
import queue


'''
h(s) = s1*a^(n-1)+s2*a^(n-2)+s3*a^(n-3) ... +s(n-1)*a+sn

s1 * a^3 + s2 * a^2 + s3 * a^1 + s4 * a^0
'''


def getHash(str, a, m):
  hash = 0
  aa = 1

  for i in range(len(str)):
    s = ord(str[i])
    hash = (hash * a % m + s)

  return hash % m


a = 1000
m = 123987123

def solution(a, m):
  q = queue.Queue()
  dic = {}
  # make string 
  s = ""
  cnt = 1000
  while True:
    for i in range(97,123):
      c = chr(i)
      s2 = s+c
      q.put(s2)
      h = getHash(s2, a, m)
      if dic.get(h) == None:
        dic[h] = s2
      else:
        cnt -= 1
        if (cnt == 0):
          print(dic[h])
          print(s2)
          return
    s = q.get()

solution(a, m)
# print(getHash('aa',a,m))
# print(getHash('ahoer',a,m))
