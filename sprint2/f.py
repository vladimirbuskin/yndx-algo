from node import Node
# from node import DoubleConnectedNode

class StackMax:
  def __init__(self):
    data = []
    sorted = []
    max = None

  def push(self, value):
    self.data.append(value)

  def pop(self):
    return self.data.pop()

  def get_max():
    return None


#def solution(node: DoubleConnectedNode) -> DoubleConnectedNode:
def solution(node, index, value):
  head = node
  newNode = Node(value)

  if index == 0:
    newNode.next = node
    return newNode

  while index-1:
    node = node.next
    index -= 1

  saved = node.next
  node.next = newNode
  newNode.next = saved

  return head

'''
[1] => [2] => [3]
       [N]
i = 1
'''
