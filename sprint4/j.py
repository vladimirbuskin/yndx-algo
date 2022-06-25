# 1 2 2 3 4 5 5 5
import random



A = 10
# ar = [1,4,6,5,9]
ar2 = [1,2,4,6,0,5,9]

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

def find4th(x, A):
  history = set()
  n = len(x)
  x.sort()
  triples = set()
  for i in range(n):
    for j in range(i+1,n):
      for k in range(j+1,n):
        target = A - x[i] - x[j] - x[k]
        if target in history:
          triples.add((target, x[i], x[j], x[k]))
    history.add(x[i])
  return triples

#print(findPairs(ar2, A))

#[1 2 3 4 5 6 7 8]

# def prepFile():
#   lines = []
#   f1 = open("j.txt", "a")
#   for i in range(1000):
#     lines.append(random.randint(0,10000))
#   lines.sort()
#   lines = map(lambda x: str(x)+"\n", lines)
#   f1.writelines(lines)
#   f1.close()
#prepFile()

numbers = []
for i in range(1000):
  numbers.append(int(input()))

print(find4th(numbers, 500))