#from node import Node

def print_range(node, l, r):
  if node == None:
    return
  goleft = node.value >= l
  goright = node.value <= r

  if goleft:
    print_range(node.left, l, r)
  if l <= node.value <= r:
    print(node.value)
  if goright:
    print_range(node.right, l, r)
