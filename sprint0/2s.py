# 1 2 2 3 4 5 5 5



A = 10
# ar = [1,4,6,5,9]
ar2 = [1,2,4,6,0,5,9]

def findPairs(x, A):
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

def findPairs2(x, A):
  history = set()
  n = len(x)
  x.sort()
  triples = set()
  for i in range(n):
    for j in range(i + 1, n):
      target = A - x[i] - x[j]
      if target in history:
        # Заметим, что тут тройка уже отсортирована за счёт предварительной
        # сортировки всего массива.
        triples.add((target, x[i], x[j]))
    history.add(x[i])
  return triples 

print(findPairs(ar2, A))