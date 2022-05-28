# from node import Node
# from node import DoubleConnectedNode

#def solution(node: DoubleConnectedNode) -> DoubleConnectedNode:
def solution(node):
  prev = None
  while node != None:
    prev = node
    node = node.next
    prev.next, prev.prev = prev.prev, prev.next
  return prev


'''
testcases
a <-> b <-> c
a <-> b
a
'''