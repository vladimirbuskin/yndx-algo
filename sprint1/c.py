import sys
from typing import List

def solution(matrix: List[List[int]], r: int, c: int) -> str:
  cn = len(matrix[0])
  rn = len(matrix)
  res = []
  # top
  if r - 1 >= 0:
    res.append(matrix[r - 1][c])
  # right
  if c + 1 < cn:
    res.append(matrix[r][c + 1])
  # bottom
  if r + 1 < rn:
    res.append(matrix[r + 1][c])
  # left
  if c - 1 >= 0:
    res.append(matrix[r][c - 1])
  return " ".join([str(x) for x in sorted(res)])


n = int(input())
m = int(input())

matrix = []
for i in range(n):
  line = sys.stdin.readline().rstrip()
  row = [int(x) for x in line.split(" ")]
  matrix.append(row)

r = int(input())
c = int(input())

print(solution(matrix, r, c))