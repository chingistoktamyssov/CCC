boxes = []
for i in range(int(input())):
  box = [int(x) for x in input().split()]
  box.sort()
  boxes.append(box)

for k in range(int(input())):
  item = [int(x) for x in input().split()]
  item.sort()
  x = 0
  truevolume = 0
  for i in boxes:
    found = True
    for j in range(2, -1, -1):
      if i[j] < item[j]:
        found = False
        break
        
    if found == True:
      x += 1
      volume = 1
      for j in i:
        volume *= j
      if x == 1:
        truevolume = volume
      else:
        truevolume = min(truevolume, volume)
        
  if truevolume == 0:
    print('Item does not fit.')
  else:
    print(truevolume)