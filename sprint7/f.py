n, k = map(int, input().split())


kk = 10**9 + 7

def calc(n, k):

  ar = { 0:1, 1:1 }

  c = 0

  # calculate all steps from 3
  for i in range(2, n + 1):
    
    # ar[4] = ar[1] + ar[2] + ar[3]
    # ar[5] = ar[2] + ar[3] + ar[4]
    # ar[6] = ar[3] + ar[4] + ar[5]
    # if ar[n] not yet calculated
    if ar.get(i, None) == None:
      c = 0
      for j in range(k, 0, -1):
        c = (c + ar.get(i - j, 0))
      ar[i] = c % kk

  r = ar.get(n)
  print(r)

calc(n-1, k)
