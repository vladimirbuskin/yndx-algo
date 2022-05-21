import sys
''' 
## F. Палиндром
## ALGO
li=0, ri=len(str)-1
while (True)
  skip (other than letters and digits) left
  skip (other than letters and digits) right
  if ri-li <= 1: 
    break
  if str[ri] != str[li]: 
    return False
  ri-=1
  li+=1
return True
'''
str = sys.stdin.readline().rstrip()

def solution(text: str) -> bool:
  text = text.lower()
  li=0
  ri=len(text)-1
  while (True):
    # skip nonLettersDigits from Left
    while li < len(text) and not isGoodChar(text[li]): li+=1
    # skip nonLettersDigits from right
    while ri >= 0 and not isGoodChar(text[ri]): ri-=1
    # check end
    if ri-li <= 0: 
      break
    # if symbols are not equal, it is not Palindrome
    if text[ri] != text[li]: 
      return False
    # move indexes
    ri-=1
    li+=1
  return True

def isGoodChar(ch: str) -> bool:
  return (ch>='0' and ch<='9') or (ch>='a' and ch<='z')

# output
print(solution(str))