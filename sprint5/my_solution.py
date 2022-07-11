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