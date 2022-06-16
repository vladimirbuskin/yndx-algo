
'''
1 2 4 5 8
10 12 14 15 17 19
'''

'''

# move until both ranges are zero
while r1-l1<=0 and r1-l1<=0:
  
  m1 = l1 + (r1-l1) // 2
  m2 = l2 + (r2-l2) // 2

  # first array median value smaller
  if ar[m1] < ar[m2]:
    # if BS1 has right side
    if r1-l1 > 0:
      # in BS1 take right part
      continue
    # if BS2 has left side
    if r2-l1 > 0:
      # in BS2 take left part
      continue

  # second array median value bigger
  if ar[m1] > ar[m2]:
    # if BS1 has right side
    if r1-l1 > 0:
      # in BS1 take left part
      continue
    # if BS2 has left side
    if r2-l1 > 0:
      # in BS2 take right part
      continue

med = 0
if len(ar1)+len(ar2) % 2 == 0:
  # take two values devide by 2
else
  # take one value


'''

def solution(ar1, ar2, 0, ):
  
  return

n = int(input())
ar1 = [int(x) for x in input().split(" ")]
m = int(input())
ar2 = [int(x) for x in input().split(" ")]
solution(ar1, ar2)

