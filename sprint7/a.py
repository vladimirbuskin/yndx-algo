
n = int(input())
#ar = map(int, input().split())
ar = [int(x) for x in input().split()]

sum = 0

if len(ar) > 0:
  b = ar[0]
  s = ar[0]
  for i in range(1, len(ar)):
    c = ar[i]
    # if next more we remember new sell price
    if c >= s:
      # continue
      s = c
    else:
      # sell
      #remember current as buy
      sum = sum + (s - b)
      b = c
      s = c
# last sale
sum = sum + s - b

print(sum)

