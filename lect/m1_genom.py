_data = """6
C C A T G A T C
2"""

def input():
  global _data
  if type(_data) is str:
    _data = _data.split("\n")
  return _data.pop(0)

# =================================================

n = int(input())
ar = list(input().split())
k = int(input())


def find (sequence, left, right):
  cumulative_sums = [0]
  cg_count = 0
  for position in range(0, len(sequence)):
    if (sequence[position] == 'C') or (sequence[position] == 'G'):
      cg_count += 1
    cumulative_sums.append(cg_count)

  print(cumulative_sums)
  return cumulative_sums[right] - cumulative_sums[left]

print(find(ar, 0, 4))


