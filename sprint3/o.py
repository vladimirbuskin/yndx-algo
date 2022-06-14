'''

'''

# 1 2 3
#   1 2

'''
k = 1
i = 0
count = 2
'''

def solution2(ar, k):
  ar.sort()
  k = k - 1
  # diff between nodes
  for i in range(1, len(ar)):
    count = len(ar)-i
    if k < count:
      pairs = []
      for j in range(0,len(ar)-i):
        pairs.append(ar[j+i] - ar[j])
      pairs.sort()
      return pairs[k]
    else:
      k -= count

def solution(ar, k):
  # print(len(ar), k)
  # exit()

  ar.sort()
  # exit()

  k = k - 1
  # diff between nodes
  diffs = []
  findAllLower = -1
  for i in range(1, len(ar)):

    mn = 1000000
    # diff = []
    for j in range(0,len(ar)-i):
      d = ar[j+i] - ar[j]
      diffs.append(d)
      # diff.append(d)
      mn = min(mn, d)

    # print(diffs, diff, mn, k)

    # ready to OUTPUT
    if not findAllLower == -1 and mn > findAllLower:
      diffs.sort()
      # print("found", diffs, mn)
      return diffs[k]

    # find all LOWER
    if findAllLower == -1 and k < len(diffs):
      diffs.sort()
      findAllLower = diffs[k]
      print("find all lower", findAllLower, len(diffs))

    # to keep
    # if (len(diffs) > 10000):
    toKeep = list(filter(lambda x : x >= mn, diffs))
    df = len(diffs) - len(toKeep);
    if k - df > 0:
      k -= len(diffs) - len(toKeep)
      diffs = toKeep

  return diffs[k]

n = int(input())
ar = [int(x) for x in input().split(" ")]
k = int(input())
print(solution(ar, k))
