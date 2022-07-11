# Comment it before submitting
class Node:  
    def __init__(self, value, left=None, right=None):  
        self.value = value  
        self.right = right  
        self.left = left

def solution(root) -> int:
    list = []
    calcPath(root, root.value, list)
    return sum(list)

def calcPath(root, path, list):
  if root.left == None and root.right == None:
    list.append(path)
  if root.left != None:
    calcPath(root.left, path * 10 + root.left.value, list)
  if root.right != None:
    calcPath(root.right, path * 10 + root.right.value, list)

def test():
    node1 = Node(2, None, None)
    node2 = Node(1, None, None)
    node3 = Node(3, node1, node2)
    node4 = Node(2, None, None)
    node5 = Node(1, node4, node3)
    assert solution(node5) == 275
test()


'''
10
0 4 1 2
1 1 3 None
2 6 None 4
3 3 5 6
4 4 7 8
5 2 None None
6 3 None None
7 7 None None
8 8 9 None
9 8 None None
'''