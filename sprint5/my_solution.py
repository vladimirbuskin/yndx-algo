def solution(root) -> bool:
  return isSearchTree(root, -1000000000, 1000000000)

def isSearchTree(root, left, right) -> bool:
  if root == None:
    return True

  if root.value <= left or root.value >= right:
    return False

  return isSearchTree(root.left, left, root.value) and isSearchTree(root.right, root.value, right)



2

  1
2
  1
    2

3
===================
  2
1   3

1
   2
      3

     3
   2
 1

