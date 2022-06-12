
'''
6 3 3 2
5 3 7 2 8 3

8 7 5 3 3 2
'''

def solution(sides):
  i = 0
  mx = 0
  sides.sort(reverse = True)
  for i in range(len(sides) - 2):
    c = sides[i]
    b = sides[i+1]
    a = sides[i+2]
    if c < (a + b):
      return c + a + b
  return mx


n = int(input())
sides = [int(x) for x in input().split(" ")]
print(solution(sides))
