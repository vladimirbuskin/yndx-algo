import sys

'''
n - number of parenthesis left to add
nop - number of opened parentesis right now

# base case
if i == len(str):
  all.push("".join(pref))

# recursive case
options = mapping(str[i])
for i in range(len(options))
  copy = pref.copy()
  combinations(str, i+1, pref)

'''

mapping = {
  '2':'abc',
  '3':'def',
  '4':'ghi',
  '5':'jkl',
  '6':'mno',
  '7':'pqrs',
  '8':'tuv',
  '9':'wxyz'
}

def combinations(str, i, pref, all):
  if i == len(str):
    all.append("".join(pref))
    return
  options = mapping[str[i]]
  for j in range(len(options)):
    combinations(str, i+1, [*pref, options[j]], all)

def solution(str):
  all = []
  combinations(str, 0, [], all)
  return all

n = input()
print(" ".join(solution(n)))
