
def findPairs(x, A):
  history = set()
  n = len(x)
  x.sort()
  triples = set()
  for i in range(n):
    target = A - x[i]
    if target in history:
      triples.add((target, x[i]))
    history.add(x[i])
  return triples

def find3th(x, A):
  history = set()
  n = len(x)
  x.sort()
  triples = set()
  for i in range(n):
    for j in range(i+1,n):
      target = A - x[i] - x[j]
      if target in history:
        triples.add((target, x[i], x[j]))
    history.add(x[i])
  return triples

'''
#8

2 3 2 4 1 10 3 0

10

'''

def find4th(x, A):
  n = len(x)
  x.sort()
  res = set()
  history = {}
  for i in range(n-1):
    for j in range(i+1,n):
      # 3 = 5 - 1 - 1
      sum = x[i] + x[j]
      target = A - sum
      if target in history:
        #print("HIST",history)
        for v in history[target]:
          tup = tuple(sorted((v[0],v[1],x[i],x[j])))
          #print('OUT',tup)
          res.add(tup)

    # add pairs we saw already
    for k in range(i):
      sum = x[k] + x[i]
      if history.get(sum) == None: history[sum] = set()
      history[sum].add((x[k], x[i]))

  return sorted(res)
  #return res


# n = int(input())
# A = int(input())
# numbers = [int(x) for x in input().split()]

A = 10000
numbers=[]
for i in range(1000):
  numbers.append(int(input()))

res = find4th(numbers, A)
print(len(res))
for r in res:
  #print(" ".join(map(str,r)))
  #print(*r)
  pass