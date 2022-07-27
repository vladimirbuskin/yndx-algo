# посылка 69447615

# Comment it before submitting
# class Node:  
#   def __init__(self, left=None, right=None, value=0):  
#     self.right = right
#     self.left = left
#     self.value = value

'''
-- ПРИНЦИП РАБОТЫ --
я сделал реализацию Удаления вершины из бинарного дерева с помощью 3х функций.
- remove - загаловочная функция, нужна только для первого вызова рекурсивной removeIn
потомучто сигнатура основной функции removeIn отличается от функции которую необходимо реализовать
- removeIn - рекурсивная функция реализующая удаление узла из дерева.
  так как у нас нет указателя на родител в узле дерева, решено было сделать параметр Parent 
  и передавать предка через него, один уровень вверх это всё что нам надо чтобы поправить ссылки после удаления узла
- takeRightMost - функция которая удаляет и возвращает самый правый элемент из переданного узла,
  если у узла есть левый потомок, он присоединяется к правому поддереву родителя.
  с помощью этой функции мы достаём самый правый элемент левого поддерева.
  в базовом случае этого рекурсивного метода текущий узел
более детальное объяснение каждого условия я добавил в комментарии самой функции.

-- ВРЕМЕННАЯ СЛОЖНОСТЬ --
временная сложность данного алгоритма Log(N) так как при вызовах методов removeIn и takeRightMost 
мы лишь раз спускаемся на полную глубину двоичного дерева

-- ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ --
пространственная сложность данного алгоритма O(Log(N)) так как максимальная глубина сбалансированного дерева с 
кол-вом элементов N является Log(N)
'''

def remove(root, key):
  return removeIn(root, None, key)

def removeIn(node, parent, key):
  if node == None:
    return None
  
  # if we found the node
  if node.value == key:
    # берём самый правый элемент из правого поддерева
    rightMost = takeRightMost(node.left)
    # если самый правый найден
    if rightMost != None:
      '''
     удаляем: 6
      дерево: 6
             / \
            2   9
           / \
          2   4
             /
            3
      '''
      # rightmost - самый правый в левом поддереве
      # rightmost узел, заменяет текущий узел, тоесть получает левое и правое поддерево текущего узла
      # если же он уже является левым потомком текущего узла, не меняем, так как он уже на своём месте.
      if node.left != rightMost:
        rightMost.left = node.left
      
      rightMost.right = node.right
    '''
    delete: 1
    tree:   1
              2
    '''
    # правого элемента в левом поддереве нет,
    # возвращаем правое поддерево
    if rightMost == None:
      rightMost = node.right

    # если родителя нет
    if parent != None:
      # Присваеваем новый узел к родителю. Если мы были в левом поддереве то в левое иначе в правое.
      # Если левое поддерево отсутствовало и rightMost пустой, то берём правое поддерево текущего узла
      if parent.left == node:
        parent.left = rightMost or node.right
      if parent.right == node:
        parent.right = rightMost or node.right
    # отчищаем ссылки удаляемого узла, для чистоты :)
    # хотя скорее всего на garbage collection не повлияет
    # так как указателей на этот объект не остаётся
    node.left = None
    node.right = None
    return rightMost
  
  # если искомое значение меньше значения в текущем узле
  # GO LEFT
  if key < node.value:
    remleft = removeIn(node.left, node, key)
  # если искомое значение больше значения в текущем узле
  # GO RIGHT
  if key > node.value:
    remRight = removeIn(node.right, node, key)
  
  return node

def takeRightMost(node, parent = None):
  if node == None:
    return None
  # это лист, удаляем ссылку на него в паренте если парент есть.
  '''
    5
  1  
    3
  '''
  if node.right == None and node.left == None:
    if parent != None:
      parent.right = None
    return node

  # у нас есть только левое поддерево, оно становится правым поддеревом родителя
  '''
    5
  1  
    3
  2
  '''
  if node.right == None:
    if parent != None:
      parent.right = node.left
      node.left = None
    return node

  # если есть правое дерево, продолжаем идти вправо
  return takeRightMost(node.right, node)

def test(root, key):
  newHead = remove(root, key)
  return newHead

def readInput():
  mode = input()
  n = int(input())
  map = {}
  root = None
  for i in range(n):
    [ i, v, l, r ] = input().split()
    map[i] = [Node(None, None, int(v)), (l), (r)]
    if root == None:
      root = map[i][0]
  for [k,[node, li, ri]] in map.items():
    if li!='-1':
      node.left = map[li][0]
    if ri!='-1':
      node.right = map[ri][0]
  return root

def printTree(root):
  if root == None:
    return
  printTree(root.left)
  print(root.value)
  printTree(root.right)

# printTree(test(readInput(), 1))