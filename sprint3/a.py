import sys

'''
n - number of parenthesis left to add
nop - number of opened parentesis right now

# base case
n == 0:
  # we got result

# recursive case for "("
if n - nop >= 2:
  # add open parentesis

# recursive case for ")"
if nop > 0:
  # add close parentesis

'''

def parentesis(n, nop, a, all):
  if n == 0:
    print("".join(a))
    return
  if n - nop >= 2:
    b = a.copy()
    b.append('(')
    parentesis(n-1, nop+1, b, all) # n-3  nop=3
  if nop > 0:
    b = a.copy()
    b.append(')')
    parentesis(n-1, nop-1, b, all)

def solution(n):
  all = []
  parentesis(n*2, 0, [], all)
  return all

n = int(input())
solution(n)
