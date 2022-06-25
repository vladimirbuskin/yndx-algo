import sys

'''

hash(abcd) = a*p^3 + b*p^2 + c*p^1 + d*p^0
hash(ab) = a*p^1 + b*p^0
hash(a) = a*p^0

hash(cd) = hash(abcd) - hash(ab)*p^2
hash(c) = hash(abc) - hash(ab)

'''

class SubstringHashCalculator:

  def __init__(self, a, m, str):
    self.a = a
    self.m = m
    self.hashes = [0]*len(str)
    self.powers = [0]*len(str)
    self.str = str
  
  def precalc(self):
    h = 0
    k = 1
    n = len(self.str)
    for i in range(len(self.str)):
      h = (h * self.a + ord(self.str[i])) % self.m
      self.hashes[i] = h
      self.powers[i] = k
      k = k*self.a % m

  def getHash(self, l, r):
    n = len(self.str)

    # hash(abcd) - len(self.str)-1
    
    # ["a","ab","abc","abcd"]

    # 1 - 2 => ab
    # 3 - 4 => cd

    # 3 - 4 | hash(cd) = hash(abcd) - hash(ab)
    # 1 - 2 | hash(ab) = hash(ab) - hash()
    # 2 - 4 | hash(bcd) = hash(abcd) - hash(a)*aa
    # 1 - 1 | hash(a) = hash(a) - hash("")

    right = 0
    if l > 1:
      #aa = a ** (r-l+1)
      aa = self.powers[r-l+1]
      right = self.hashes[l-2] * aa % self.m
    
    #print(self.powers)

    return (self.hashes[r-1] + self.m - right) % self.m

a = int(input())
m = int(input())
str = input()
n = int(input())

hashCalc = SubstringHashCalculator(a, m, str)
hashCalc.precalc()

for i in range(n):
  l, r = map(int, input().split())
  print(hashCalc.getHash(l, r))

