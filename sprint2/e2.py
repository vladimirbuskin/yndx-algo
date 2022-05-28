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


def insert(head, index, value):
  newNode = Node(value)

  if index == 0:
    newNode.next = head
    return newNode

  prev = findElem(head, index-1)

  newNode.next = prev.next
  prev.next = newNode
  
  return head

def findElem(node, index):
  while index and node.next != None and node.next.next != None:
    node = node.next
    index -= 1
  return node

def deleteByIndex(head, index, value):

  if index == 0:
    newHead = head.next
    head.next = None
    return newHead

  prev = findElem(head, index-1)
  prev.next = prev.next.next

  return head


'''
[1] => [2] => [3]
       [N]
i = 1
'''
