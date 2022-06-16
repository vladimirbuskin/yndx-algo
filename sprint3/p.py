'''
[3, 2, 0, 1, 4, 6, 5]

move left to right save max
3 3 3 3 4 6 6

move right to left save min
0 0 0 1 4 5 5
n = 3


1  9  40 30 

1  9  40 40

40 40 40 30


0 1 3 2
-------
0 1 3 3
0 1 2 2

3

3 6 7 4 1 5 0 2
---------------
0 0 0 0 0 0 0 2
3 6 7 7 7 7 7 7

1

1 0 2 3 4
---------
0 0 2 3 4
1 1 2 3 4

4




i = 4
mx = 4
'''
def solution(ar):
  
  # [3, 0, 0, 1, 4, 6, 5]

  # move left to right save max
  # 3 3 3 3 4 6 6
  # move right to left save min
  # 0 0 0 1 4 5 5


  ar_min = [0]*len(ar)
  ar_max = [10**19]*len(ar)

  # move left to right save max
  # 3 3 3 3 4 6 6
  mx = 0
  for i in range(len(ar)):
    mx = max(mx, ar[i])
    ar_max[i] = mx

  # move right to left save min
  # 0 0 0 1 4 5 5
  mn = 10**19
  for i in range(len(ar)-1, -1, -1):
    mn = min(mn, ar[i])
    ar_min[i] = mn

  # print("".join(map(lambda x: str(x).ljust(5), ar_min)))
  # print("".join(map(lambda x: str(x).ljust(5), ar_max)))
  
  # move from left, check if both numbers have changed, +1 if one didnt change keep going
  cnt = 1
  mn = ar_min[0]
  mx = ar_max[0]
  for i in range(1, len(ar)):
    # numbers are different and 
    # min from numbers on the left lower than numbers on the right - so ranges are rising
    if ar_min[i] != mn and ar_max[i] != mx and (max(mn,mx) < min(ar_min[i],ar_max[i])):
      cnt+=1
    mn = ar_min[i]
    mx = ar_max[i]

  return cnt

n = int(input())
ar = [int(x) for x in input().split(" ")]
print(solution(ar))
