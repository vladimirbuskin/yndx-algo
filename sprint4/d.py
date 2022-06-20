import sys

'''
'''

def solution(strings):
  dic = {}
  for s in strings:
    dic[s] = 1

  for k in dic:
    print(k)

n = int(input())
strings = []
for i in range(n):
  strings.append(input())

solution(strings)

