from c import solution
from node import Node, listCount, listPrint, listPrintFlat

def test():
  count = int(input())

  head = None
  node = None
  for i in range(count):
    if head == None:
      node = head = Node(input())
    else:
      node = Node(input(), node)
  
  toDelete = int(input())
  
  h = solution(node, toDelete)
  listPrintFlat(h)
  # print(listCount(h))


test()
