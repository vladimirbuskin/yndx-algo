from b import solution
from node import Node

def test():
  n3 = Node("hello")
  n2 = Node("Word", n3)
  n1 = Node("some", n2)
  solution(n1)
  
test()