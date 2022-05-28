
class Node:
    def __init__(self, value, next=None):  
        self.value = value  
        self.next = next

class DoubleConnectedNode:  
    def __init__(self, value, next=None, prev=None):  
        self.value = value  
        self.next = next  
        self.prev = prev

def listPrint(node):
  while node != None:
    print(node.value, end="")
    node = node.next
    if node != None:
      print(" -> ", end="")
  print("")

def listDoublePrint(node: DoubleConnectedNode):
  while node != None:
    print(node.value, end="")
    node = node.next
    if node != None:
      print(" <-> ", end="")
  print("")

def listPrintFlat(node):
  while node != None:
    print(node.value)
    node = node.next

def listCount(node):
  c = 0
  while node != None:
    node = node.next
    c += 1
  return c