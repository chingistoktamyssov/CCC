moves = [[+1, +2], [+1, -2], [+2, +1], [+2, -1], [-1, +2], [-1, -2], [-2, +1], [-2, -1]]
a = []
z = True
s = 0

start = [[int(x) for x in input().split()]]
end = [int(x) for x in input().split()]

a = start

if a.count(end) == 1:
  print(0)
  z = False
  
while z == True:
  s = s + 1
  for j in range(len(a)):
    for i in range(8):
      if 1 <= a[j][0]+moves[i][0] <= 8 and 1 <= a[j][1]+moves[i][1] <= 8 and a.count([a[j]      [0]+moves[i][0], a[j][1]+moves[i][1]]) == 0:
        a.append([a[j][0]+moves[i][0], a[j][1]+moves[i][1]])
        if a.count(end) == 1:
          print(s)
          z = False
          break
    if z == False:
      break
