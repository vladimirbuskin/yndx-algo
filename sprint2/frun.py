from f import solution
from node import Node, listPrint

def test():
  n1 = Node("node1")
  n2 = Node("node2")
  n3 = Node("node3")
  n1.next = n2
  n2.next = n3


  head = n1
  listPrint(head)

  head = solution(head, 3, "NEW")
  listPrint(head)


test()