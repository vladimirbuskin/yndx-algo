# Comment it before submitting
# class Node:  
#     def __init__(self, value, left=None, right=None):  
#         self.value = value  
#         self.right = right  
#         self.left = left

def solution(root):
  if root == None:
    return -9000000000
  return max(root.value, solution(root.left), solution(root.right))

# def findBiggest(root, mx):
#   if root == None:
#     return mx
#   mx = max(mx, root.value)
#   mx = findBiggest(root.left, mx)
#   mx = findBiggest(root.right, mx)
#   return mx

# def test():
#     node1 = Node(1)
#     node2 = Node(-5)
#     node3 = Node(3, node1, node2)
#     node4 = Node(2, node3, None)
#     print(solution(node4))
#     assert solution(node4) == 3

# test()