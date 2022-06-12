
from re import I


i = 10000

def aa(x):
  global i
  i -= 1
  return x + i

n = " ".join(map(str,map(aa,[0]*10000)))
print(i)
print(n)
print(i)
print(n)
