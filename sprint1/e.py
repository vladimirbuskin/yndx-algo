import sys

# === ALGO ===
# for in range[len(str)]
#   if space move pointer to i + 1
#   if not space
#     if word is longer, remember cur word
count = int(input())
text = sys.stdin.readline().rstrip()

def solution(text: str) -> int:
  maxLen = 0
  word = [0, 0]
  stIndex = 0
  for i in range(len(text)):
    if text[i] == ' ':
      stIndex = i + 1
    else:
      if i + 1 - stIndex > maxLen:
        maxLen = i + 1 - stIndex
        word[0] = stIndex
        word[1] = i + 1
  return text[word[0]:word[1]]

word = solution(text)

# output
print(word)
print(len(word))