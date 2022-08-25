n = int(input())

events = []

for i in range(n):
  start,end = [float(x) for x in input().split()]
  events.append([end, start])


res = []
events.sort()

ev = events[0]
for i in range(1, len(events)):
  c = events[i]
  # find new range
  
  # if current event starts later or at the same time, make this prev
  if c[1] >= ev[0]:
    res.append(ev)
    ev = c

res.append(ev)

print(len(res))
for r in res:
  print(r[1], r[0])

'''
9 10
9.3 10.3
10 11
10.3 11.3
11 12

'''