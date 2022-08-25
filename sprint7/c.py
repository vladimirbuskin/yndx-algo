m = int(input())
n = int(input())

heaps = []

for i in range(n):
  price,kg = [int(x) for x in input().split()]
  heaps.append([price, kg])


res = []
heaps.sort(key=lambda x: -x[0])

left = m
money = 0

for i in range(len(heaps)):
  price, kg = heaps[i]
  # find new range
  if kg < left:
    left -= kg
    money += price * kg
  else:
    money += price * left
    left = 0
    break
'''
price: 2
kg: 10

left: 4
money: 8 + 20
'''

print(money)