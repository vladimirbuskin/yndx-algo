def solution(str):
  mapOpen = {
    "(":1,
    "[":1,
    "{":1
  }
  mapClose = {
    ")":"(",
    "]":"[",
    "}":"{"
  }
  stack = []
  for i in range(len(str)):
    ch = str[i]
    # is open
    if mapOpen.get(ch) != None:
      stack.append(ch)
      continue
    # is close
    if mapClose.get(ch) != None:
      if len(stack) == 0 or mapClose.get(ch) != stack.pop():
        return False
  return len(stack) == 0

# process input
print(solution(input()))
