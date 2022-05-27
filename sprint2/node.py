
class Node:
    def __init__(self, value, next_item=None):  
        self.value = value  
        self.next_item = next_item

def listPrint(node):
  while node != None:
    print(node.value, end="")
    node = node.next_item
    if node != None:
      print(" -> ", end="")
  print("")

def listPrintFlat(node):
  while node != None:
    print(node.value)
    node = node.next_item

def listCount(node):
  c = 0
  while node != None:
    node = node.next_item
    c += 1
  return c