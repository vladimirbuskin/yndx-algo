from typing import List

def solution(mat: List[List[int]]) -> int:
  if (len(mat) > 0):
    for c in range(len(mat[0])):
      ar = []
      for r in range(len(mat)):
        ar.append(mat[r][c])
      print(*ar);


# read data
r = int(input())
c = int(input())
mat = []
for i in range(r):
  mat.append(input().split(" "));

solution(mat)

'''
ALGO

for c in [0..len(mat[0]))
  for r in [0..len(mat))
    ar.append(mat[r][c])
    print(*ar);

'''
