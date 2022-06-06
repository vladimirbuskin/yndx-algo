import sys

class Node:
  def __init__(self, value):
    self.value = value
    self.next = None
    self.prev = None
    return None

# [n1] <-> [n2]
# [n1]

class MyQueueList:
  def __init__(self):
    self.head = None
    self.tail = None
    self.sz = 0

  def put(self, value):
    if self.head == None:
      self.head = self.tail = Node(value)
    else:
      node = Node(value)
      node.next = self.tail
      self.tail.prev = node
      self.tail = node
    self.sz += 1

  def get(self):
    if self.head == None:
      return "error"
    if self.head != None:
      value = self.head.value
      # get 
      self.head = self.head.prev
      # if this is last element
      if self.head == None:
        self.tail = None
      else:
        self.head.next = None
      self.sz -= 1
    return value

  def size(self):
    return self.sz

opsCount = int(input())

queue = MyQueueList()

output = []
for i in range(opsCount):
  ar = sys.stdin.readline().rstrip().split()
  if ar[0] == "put":
    out = queue.put(ar[1])
    if (out): output.append(out)
  if ar[0] == "size":
    output.append(str(queue.size()))
  if ar[0] == "get":
    output.append(queue.get())

print("\n".join(output))