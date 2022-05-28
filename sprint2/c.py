#from node import Node

def solution(node, idx: int):
  head = node
  # delete zero element
  if idx == 0: 
    node = node.next
    head = node
    return head
  
  i = 0
  # delete 1 > 0 elements
  while node != None:
    if i + 1 == idx and node.next != None:
      node.next = node.next.next
      return head
    node = node.next
    i += 1

  return head

'''
testcases
a -> b -> c
a -> b
a
'''