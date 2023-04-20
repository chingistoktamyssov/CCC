trout, pike, pickerel = int(input()), int(input()), int(input())
maximum = int(input())

combinations = []

for a in range(0, maximum // pickerel + 1):
  for b in range(0, maximum // pike + 1):
    for c in range(0, maximum // trout +1):
      if 0 < a*pickerel + b*pike + c*trout <= maximum:
        combinations.append([c, b, a])

for i in combinations:
  print(i[0], 'Brown Trout,', i[1], 'Northern Pike,', i[2], 'Yellow Pickerel')

print('Number of ways to catch fish:', len(combinations))