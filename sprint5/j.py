# Comment it before submitting
class Node:  
  def __init__(self, left=None, right=None, value=0):  
    self.right = right
    self.left = left
    self.value = value

def insert(root, key):
  # base cases
  if root == None:
    return

  if key < root.value:
    if root.left == None:
      # insert left
      root.left = Node(None, None, key)
    else:
      insert(root.left, key)

  if key >= root.value:
    if root.right == None:
      # insert right
      root.right = Node(None, None, key)
    else:
      insert(root.right, key)

  return root

def printTree(root):
  if root == None:
    return
  print(root.value)
  print("Go left")
  printTree(root.left)
  print("Go right")
  printTree(root.right)

def test():
    node1 = Node(None, None, 7)
    node2 = Node(node1, None, 9)
    node3 = Node(None, node2, 7)
    new_head = insert(node3, 7)
    printTree(new_head)

test()