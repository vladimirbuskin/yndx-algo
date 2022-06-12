
def solution(children, cookies):
  children.sort()
  cookies.sort()
  i = 0
  j = 0
  s = 0
  while i < len(children) and j < len(cookies):
    if children[i] <= cookies[j]:
      s += 1
      i += 1
      j += 1
    else:
      j += 1
  return s

n = int(input())
children = [int(x) for x in input().split(" ")]
m = int(input())
cookies = [int(x) for x in input().split(" ")]

print(solution(children, cookies))
