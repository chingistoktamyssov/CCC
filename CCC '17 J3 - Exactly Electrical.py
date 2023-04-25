point1 = input().split()
point2 = input().split()
charge = int(input())

a, b = int(point1[0]), int(point1[1])
c, d = int(point2[0]), int(point2[1])

steps = abs(a - c) + abs(b - d)

if (charge - steps) % 2 == 0 and (charge - steps) >= 0:
  print('Y')
else:
  print('N')