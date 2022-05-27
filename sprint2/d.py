#from node import Node

def solution(node, toFindValue):

  i = 0
  while node != None:
    if node.value == toFindValue:
      return i
    node = node.next_item;
    i += 1

  return -1

'''
testcases
a -> b -> c
a -> b
a
'''