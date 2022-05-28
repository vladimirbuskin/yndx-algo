from e import solution
from node import DoubleConnectedNode, listDoublePrint

def test():
  n1 = DoubleConnectedNode("some")
  n2 = DoubleConnectedNode("Word")
  n3 = DoubleConnectedNode("hello")

  n1.next = n2
  n2.next = n3

  n2.prev = n1
  n3.prev = n2

  head = n1
  listDoublePrint(head)

  head = solution(head)
  listDoublePrint(head)


test()