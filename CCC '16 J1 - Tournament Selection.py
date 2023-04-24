w = 0
l = 0

for i in range(6):
  game = input()

  if game == 'W':
    w = w + 1
  else:
    pass

if w == 5 or w == 6:
  print("1")
elif w == 3 or w == 4:
  print("2")
elif w == 1 or w == 2:
  print("3")
elif w == 0:
  print("-1")