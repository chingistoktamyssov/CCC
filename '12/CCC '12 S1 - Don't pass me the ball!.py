n = int(input())

count = 0

for a in range(1, n+1):
  for b in range(1, n+1):
    for c in range(1, n+1):
      if a < b < c < n:
        count += 1

print(count)