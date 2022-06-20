import sys


'''
h(s) = s1*a^(n-1)+s2*a^(n-2)+s3*a^(n-3) ... +s(n-1)*a+sn

s1 * a^3 + s2 * a^2 + s3 * a^1 + s4 * a^0
'''


def solution(str, a, m):
  hash = 0
  aa = 1

  for i in range(len(str)):
    s = ord(str[i])
    hash = (hash * a % m + s)

  return hash % m


a = int(input())
m = int(input())
str = sys.stdin.readline().rstrip()

print(solution(str, a, m))
