class StackMaxEff:
  def __init__(self):
    self.data = []
    self.maxStack = []

  def push(self, value):
    # when empty add always
    if len(self.maxStack) == 0:
      self.maxStack.append(value)
    # otherwise add only bigger element
    elif self.maxStack[-1] >= value:
      self.maxStack.append(value)
    self.data.append(value)

  def pop(self):
    if len(self.data) == 0:
      return "error"
    popValue = self.data.pop()
    if self.maxStack[-1] == popValue:
      self.maxStack.pop()
    return popValue

  def get_max(self):
    if (len(self.maxStack) == 0):
      return None
    return self.maxStack[-1]

stack = StackMaxEff()

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