
'''
1 2 3 1 2 3 4
1 1 2 2 3 3 4
cur = 1
count = 2
'''

def solution(clgs, k):
  mx = 0
  clgs.sort()
  res = []

  # make array with [num,id]
  cur = clgs[0]
  count = 1
  for i in range(1, len(clgs)):
    if cur != clgs[i]:
      res.append([count, cur])
      cur = clgs[i]
      count = 1
    else:
      count += 1
  res.append([count, cur])

  # sort array
  res.sort(key = lambda x: [-x[0],x[1]])

  # take k from head and take ids and print
  lst = list(map(lambda x: str(x[1]), res[0:k]))
  print(" ".join(lst))

n = int(input())
clgs = [int(x) for x in input().split(" ")]
k = int(input())
solution(clgs, k)
