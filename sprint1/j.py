'''
== ALGO
res = []
ost = num
n = 2
while ost > 1
  while (ost % n == 0):
    ost = int(ost / n)
    res.push(n)
  n += 1
'''

def solution(num: int) -> str:
  res = []
  ost = num
  n = 2
  while ost > 1:
    while (ost % n == 0):
      ost = int(ost / n)
      res.append(n)
    n += 1
    if n*n > num:
      break
  if (ost > 1):
    res.append(ost)
  return " ".join(map(str,res))

num = int(input())
print(solution(num))