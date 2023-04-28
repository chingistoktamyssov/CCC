delivered = int(input())
collision = int(input())

if delivered > collision:
  print(delivered * 50 - collision * 10 + 500)
else:
  print(delivered * 50 - collision * 10)