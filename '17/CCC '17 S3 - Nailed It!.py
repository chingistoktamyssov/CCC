lengths = [0] * 2001
heights = [0] * 4001

n = int(input())
boards = [int(x) for x in input().split()]

for i in boards:
  lengths[i] += 1

for i in range(1, 2001):
  for j in range(i, 2001):
    if i == j:
      heights[i+j] += lengths[i] // 2
    else:
      heights[i+j] += min(lengths[i], lengths[j])

length, height = 0, 0

for i in heights:
  if i > length:
    length = i
    height = 1
  elif i == length:
    height += 1

print(length, height)