class StackMax:
  def __init__(self):
    self.data = []

  def push(self, value):
    self.data.append(value)

  def pop(self):
    if (len(self.data) > 0):
      return self.data.pop()
    return "error"

  def get_max(self):
    if len(self.data) == 0:
      return None
    return max(self.data)

stack = StackMax()

# process input
num = int(input())
for i in range(num):
  ar = input().split()
  if ar[0] == "push":
    stack.push(int(ar[1]))
  if ar[0] == "pop":
    if stack.pop() == "error":
      print("error")
  if ar[0] == "get_max":
    print(stack.get_max())