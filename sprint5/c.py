# Comment it before submitting
# class Node:  
#     def __init__(self, value, left=None, right=None):  
#         self.value = value  
#         self.right = right  
#         self.left = left


def solution(root):
    isAnagram(root.left, root.right)

def isAnagram(left, right):
  if left == None and right == None:
    return True
  if left == None or right == None:
    return False
  if left.value != right.value:
    return False
  return isAnagram(left.right, right.left) and isAnagram(left.left, right.right)

def test():
    node1 = Node(3,  None,  None)
    node2 = Node(4,  None,  None)
    node3 = Node(4,  None,  None)
    node4 = Node(3,  None,  None)
    node5 = Node(2, node1, node2)
    node6 = Node(2, node3, node4) 
    node7 = Node(1, node5, node6)
    assert solution(node7)