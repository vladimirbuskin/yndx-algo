from d import solution
from node import Node

def test():
  n3 = Node("hello")
  n2 = Node("Word", n3)
  n1 = Node("some", n2)
  nn = Node("value")
  print(solution(n1, 'Word'))
  
test()