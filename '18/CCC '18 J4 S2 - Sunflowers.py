plants = []

def check(plants):
  correct = True
  for i in range(len(plants)):
    for j in range(len(plants)):
      if i + 1 == len(plants) or j + 1 == len(plants):
        pass
      elif plants[i][j] >= plants[i][j + 1] or plants[i][j] >= plants[i + 1][j]:
        correct = False
  return correct

def rotate(plants):
  newplants = []

  for i in range(len(plants)):
    row = []
    for j in plants:
      row.append(j[i])
    newplants.append(row)

  for i in newplants:
    i.reverse()

  return newplants

for i in range(int(input())):
  plants.append([int(j) for j in input().split()])

correct = check(plants)

while correct == False:
  plants = rotate(plants)
  correct = check(plants)

for i in plants:
  print(' '.join([str(j) for j in i]))