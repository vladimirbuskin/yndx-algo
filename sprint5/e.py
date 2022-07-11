# Comment it before submitting
class Node:  
    def __init__(self, value, left=None, right=None):  
        self.value = value  
        self.right = right  
        self.left = left

def solution(root) -> bool:
  return isSearchTree(root, -1000000000, 1000000000)

def isSearchTree(root, left, right) -> bool:
  if root == None:
    return True

  if root.value <= left or root.value >= right:
    return False

  return isSearchTree(root.left, left, root.value) and isSearchTree(root.right, root.value, right)



def test():
    node1 = Node(1, None, None)
    node2 = Node(4, None, None)
    node3 = Node(3, node1, node2)
    node4 = Node(8, None, None)
    node5 = Node(5, node3, node4)
    
    assert solution(node5)
    node2.value = 5
    assert not solution(node5)

test()