#from node import Node

def solution(node, idx: int):
  head = node
  # delete zero element
  if idx == 0: 
    node = node.next_item
    head = node
    return head
  
  i = 0
  # delete 1 > 0 elements
  while node != None:
    if i + 1 == idx and node.next_item != None:
      node.next_item = node.next_item.next_item
      return head
    node = node.next_item
    i += 1

  return head

'''
testcases
a -> b -> c
a -> b
a
'''