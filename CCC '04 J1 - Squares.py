tiles = int(input())

while True:
  remainder = (tiles ** 0.5) % 1

  if remainder == 0:
    side = str(int(tiles ** 0.5))
    print("The largest square has side length", side + ".")
    break
    
  else:
    tiles -= 1
