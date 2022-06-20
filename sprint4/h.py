import sys

'''
'''

def solution(str1, str2):
  if not (len(str1)) == len(str2):
    return "NO"
  if len(str1) < len(str2):
    str2,str1 = str1,str2
  d = {}
  d2 = {}
  for i in range(len(str1)):
    s1 = str1[i]

    s2 = str2[i]
    # if we saw symbol already
    if not d.get(s1) == None:
      # symbol must to be equal
      if not s2 == d[s1]:
        # if not equal we return "NO"
        return "NO"
    else:
      # add to dict
      d[s1] = s2
      # check that d2 does not contain it yet
      if not d2.get(s2) == None:
        return "NO"
      else:
        d2[s2] = s1

  return "YES" 

str1 = input()
str2 = input()
print(solution(str1, str2))
