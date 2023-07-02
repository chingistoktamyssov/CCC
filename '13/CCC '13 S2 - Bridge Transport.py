weight = int(input())

cars = []
for i in range(int(input())):
  cars.append(int(input()))

n = 0

while len(cars) > 0:
  if len(cars) <= 4:
    if sum(cars) <= weight:
      n += len(cars)
    break
  else:
    if sum(cars[:4]) <= weight:
      n += 1
      cars.pop(0)
    else:
      if sum(cars[:3]) <= weight:
        n += 3
      elif sum(cars[:2]) <= weight:
        n += 2
      elif sum(cars[:1]) <= weight:
        n += 1
      break

print(n)