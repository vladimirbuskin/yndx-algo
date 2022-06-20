
'''
1 2 4 5 8
10 12 14 15 17 19

0 0 0 1 3 3 5 10
4 4 5 7 7 7 8 9 9 10

0 1 2 3
1 2 3 4 5 6

0 1 1 2 2 3 3 4 5 6

0 1 2 3 30 40 50 60
1 2 3 4 5 6

0 1 2 3
11 12 16 19 22

l1: 3
r1: 4
m1: 3
m1v: 3

l2: 0
r2: 5
m2: 2
m2v: 16
'''

# we need to find index l1 or l2
mf = (len(ar1)+len(ar2)) // 2

l1 + l2 >= mf && l1 + l2 < mf + 1

m1v < m2v

'''

mf = (len(ar1) + len(ar2)) // 2

# move until both ranges are zero
while r1-l1<=0 and r1-l1<=0:
  
  m1 = l1 + (r1-l1) // 2
  m2 = l2 + (r2-l2) // 2

  # first array median value smaller, search median in ar1
  if ar[m1] < ar[m2]:
    # if ar1 has right side
    if r1-l1 > 1:
      # take ar1 right part
      continue
    # center in ar2
    if l1+l2 >= mf:
      # take ar2 left part
      continue
    else:
      # take ar2 right part
      continue
  # first array median value bigger, search median in ar2
  else:
    # if ar2 has left side
    if r2-l2 > 1:
      # in BS1 take left part
      continue
    # if BS2 has left side
    if r2-l1 > 1:
      # in BS2 take right part
      continue

med = 0
if len(ar1)+len(ar2) % 2 == 0:
  # take two values devide by 2
else
  # take one value

[1 - n], i, []

'''

def solution(ar1, ar2, 0, ):
  
  return

n = int(input())
ar1 = [int(x) for x in input().split(" ")]
m = int(input())
ar2 = [int(x) for x in input().split(" ")]
solution(ar1, ar2)

