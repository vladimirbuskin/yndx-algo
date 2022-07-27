'''
        20
    10     30
 4     15
     12
'''


'''
-- ПРИНЦИП РАБОТЫ --
я сделал реализацию Удаления вершины из бинарного дерева с помощью 3х функций.
- remove - загаловочная функция, нужна только для первого вызова рекурсивной removeIn
потомучто сигнатура основной функции removeIn отличается от функции которую необходимо реализовать
- removeIn - рекурсивная функция реализующая удаление узла из дерева.
  так как у нас нет указателя на родител в узле дерева, решено было сделать параметр Parent 
  и передавать предка через него, один уровень вверх это всё что нам надо чтобы поправить ссылки после удаления узла
- takeRightMost -

-- ВРЕМЕННАЯ СЛОЖНОСТЬ --

-- ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ --
пространственная сложность поискового индекса O(W*D)
где:
W - кол-во уникальных слов во всех документах
D - кол-во документов

пространственная сложность поиска одной фразы по индексу O(N + D)
где:
N - кол-во слов в одной поисковой фразе
D - кол-во документов


'''


# Comment it before submitting
# class Node:  
#   def __init__(self, left=None, right=None, value=0):  
#     self.right = right
#     self.left = left
#     self.value = value

def remove(root, key):
  return removeIn(root, None, key)

def removeIn(node, parent, key):
  if node == None:
    return None
  # if we found the node
  if node.value == key:
    rightMost = takeRightMost(node.left, node)
    if rightMost != None:
      rightMost.left = node.left
      rightMost.right = node.right
    if parent != None:
      # if we deleted left Node
      if parent.left == node:
        parent.left = rightMost
      # if we deleted right Node
      if parent.right == node:
        parent.right = rightMost
    # return deleted
    node.left = None
    node.right = None
    return rightMost
  
  remleft = removeIn(node.left, node, key)
  remRight = removeIn(node.right, node, key)
  
  return node

def takeRightMost(node, parent):
  if node == None:
    return None
  # this is leaf, we found it, remove it from parent
  '''
    5
  1  
    3
  '''
  if node.right == None and node.left == None:
    parent.right = None
    return node

  # we dont have right node, but have left node
  '''
    5
  1  
    3
  2
  '''
  if node.right == None:
    # take r
    parent.right = node.left
    node.left = None
    return node

  # go deeper to rightmost
  return takeRightMost(node.right, node)

def test():
  node1 = Node(None, None, 2)
  node2 = Node(node1, None, 3)
  node3 = Node(None, node2, 1)
  node4 = Node(None, None, 6)
  node5 = Node(node4, None, 8)
  node6 = Node(node5, None, 10)
  node7 = Node(node3, node6, 5)
  # newHead = remove(node7, 10)
  # print(newHead.value)
  # assert newHead.value == 5
  # assert newHead.right is node5
  # assert newHead.right.value == 8
  # newHead = remove(node7, 12)
  # assert newHead.right.value == 10
  # assert newHead.right.right is None
  # assert newHead.right.left.value == 8
  # newHead = remove(node7, 6)
  # assert newHead.right.value == 10
  # assert newHead.right.left.value == 8
  # assert newHead.right.left.left is None
  # newHead = remove(node7, 5)
  # assert newHead.value == 3
  # assert newHead.left.value == 1
  # assert newHead.left.left is None
  # assert newHead.left.right.value == 2
  # assert newHead.right.value == 10

test()