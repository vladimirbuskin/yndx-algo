def solution(k, homes):
  i = 0
  homes.sort()
  while i < len(homes) and k >= homes[i]:
    k -= homes[i]
    i += 1 
  return i


n, k = [int(x) for x in input().split(" ")]
homes = [int(x) for x in input().split(" ")]
print(solution(k, homes))
