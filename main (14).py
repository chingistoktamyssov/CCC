daytime = int(input())
evening = int(input())
weekend = int(input())

def plana(daytime, evening, weekend):
  total = 0
  if daytime - 100 > 0:
    total += (daytime - 100) * 25
  total += evening * 15
  total += weekend * 20
  total *= 0.01
  total = str(total)
  x = total.index('.')
  if len(total[x+1:]) != 2:
    total = total.ljust(2 - len(total[x+1:]) + len(total), '0')
  return total

def planb(daytime, evening, weekend):
  total = 0
  if daytime - 250 > 0:
    total += (daytime - 250) * 45
  total += evening * 35
  total += weekend * 25
  total *= 0.01
  total = str(total)
  x = total.index('.')
  if len(total[x+1:]) != 2:
    total = total.ljust(2 - len(total[x+1:]) + len(total), '0')
  return total

a = plana(daytime, evening, weekend)
b = planb(daytime, evening, weekend)

print('Plan A costs', a)
print('Plan B costs', b)

if float(a) < float(b):
  print('Plan A is cheapest.')
elif float(b) < float(a):
  print('Plan B is cheapest.')
else:
  print('Plan A and B are the same price.')