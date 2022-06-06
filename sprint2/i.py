from array import array
import sys

class MyQueueSized:
  def __init__(self, max_size):
    self.data = [0] * max_size
    self.max_size = max_size
    self.head = 0
    self.tail = 0
    self.sz = 0

  def push(self, value):
    if (self.sz == self.max_size):
      return "error"
    self.data[self.tail] = value
    self.tail = (self.tail + 1) % self.max_size
    self.sz += 1

  def pop(self):
    if (self.sz == 0):
      return "None"
    value = self.data[self.head]
    self.data[self.head] = None
    self.head = (self.head + 1) % self.max_size
    self.sz -= 1
    return value

  def peek(self):
    if (self.sz == 0):
      return "None"
    return self.data[self.head]

  def size(self):
    return self.sz

opsCount = int(input())
maxLength = int(input())

queue = MyQueueSized(maxLength)

output = []
for i in range(opsCount):
  ar = sys.stdin.readline().rstrip().split()
  if ar[0] == "peek":
    output.append(queue.peek())
  if ar[0] == "push":
    out = queue.push(ar[1])
    if (out): output.append(out)
  if ar[0] == "size":
    output.append(str(queue.size()))
  if ar[0] == "pop":
    output.append(queue.pop())

print("\n".join(output))