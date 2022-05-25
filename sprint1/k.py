import sys
import math
from typing import List

'''
== ALGO
res = []
perenos = 0
while i >= 0 or ost > 0:
  digit1 = take last digit from firstNumber
  digit2 = take last digit from secondNumber
  
  sum = digit1 + digit2 + perenos
  secondNumber = math.floor(sum / 10)
  res.push(sum % 10)
  if (i!=len(lst)-1):
    res *= 10
return res + num;
'''

def solution(lst: List, num):
  ost = num
  perenos = 0
  i = len(lst)-1
  res = []
  while i >= 0 or ost > 0:
    digit1 = lst[i] if i>=0 else 0
    digit2 = ost % 10
    ost = math.floor(ost / 10)
    
    sum = perenos + digit1 + digit2
    perenos = math.floor(sum / 10)
    res.append(sum % 10)
    i-=1

  if perenos > 0:
    res.append(perenos)
  res.reverse()

  return " ".join(map(str,res));


c = int(sys.stdin.readline().rstrip())
lst = [int(x) for x in sys.stdin.readline().rstrip().split(" ")]
num = int(sys.stdin.readline().rstrip())

print(solution(lst, num))