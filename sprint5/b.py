import math
# Comment it before submitting
class Node:  
    def __init__(self, value, left=None, right=None):  
        self.value = value  
        self.right = right  
        self.left = left

def solution(root):
  isBal = { "isBal": True }
  isBalanced(root, 0, isBal)
  return isBal["isBal"]

def isBalanced(root, level, isBal):
  if root == None:
    return level
  
  levelLeft = isBalanced(root.left, level+1, isBal)
  levelRight = isBalanced(root.right, level+1, isBal)
  
  # if for current level levels are different
  if abs(levelLeft - levelRight) > 1:
    isBal["isBal"] = False

  return max(levelLeft, levelRight)
  

def test():
    node1 = Node(1)
    node2 = Node(-5)
    node3 = Node(3, node1, node2)
    node4 = Node(10)
    node5 = Node(2, node3, node4)
    assert solution(node5)

test()