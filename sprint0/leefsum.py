_data = """6
-9 -7 -6 -1 -1 3
2"""

# _data = """8
# 6 2 8 -3 1 1 6 10
# 100"""

def input():
  global _data
  if type(_data) is str:
    _data = _data.split("\n")
  return _data.pop(0)

# =================================================

n = int(input())
ar = list(map(lambda x: int(x), input().split()))
k = int(input())


def find (ar):
  l = 0
  r = len(ar)-1
  while l<r:
    t = ar[l]
    ar[l] = ar[r]
    ar[r] = t
    l+=1
    r-=1
  return ar

#print(find(ar))


#     1
#   2   4
# 3       3

root = {
  "value": 1,
  "left": {
    "value": 2,
    "left": {
      "value": 3,
    },
    "right": None
  },
  "right": {
    "value": 4,
    "right": {
      "value": 4,
    },
    "keft": None
  },
}

# def treeSum(node):
#   if node == None:
#     return 0
#   if node.get("left") == None and node.get("right") == None:
#     return node.get("value")
#   else:
#     return treeSum(node.get("left")) + treeSum(node.get("right"))

sum = 0

# def treeSum(node):
#   global sum
#   if node == None: return
#   if node.get("left") == None and node.get("right") == None:
#     sum += node.get("value")
#   treeSum(node.get("left"))
#   treeSum(node.get("right"))
from queue import Queue

# def treeSum(node):
#   sum = 0
#   q = Queue()
#   q.put(node)
#   while not q.empty():
#     node = q.get()
#     if node.get("left") == None and node.get("right") == None:
#       sum += node.get("value", 0)
#     if node.get("left") != None: 
#       q.put(node.get("left"))
#     if node.get("right") != None: 
#       q.put(node.get("right"))
#   return sum

def treeSum(node):
  sum = 0
  stack = []
  stack.append(node)

  while len(stack) > 0:
    node = stack.pop()
    if node.get("left") == None and node.get("right") == None:
      sum += node.get("value", 0)
    
    if node.get("left") != None: 
      stack.append(node.get("left"))
    if node.get("right") != None: 
      stack.append(node.get("right"))
  return sum

print(treeSum(root))
# print (root.get("value1"));
