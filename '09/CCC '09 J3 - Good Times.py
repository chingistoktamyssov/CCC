minutes = 0

def converter(minutes):
  if int(minutes) < 0:
    minutes += 1440
  a = minutes // 600
  b = (minutes - 600 * a) // 60
  c = (minutes - 600 * a - 60 * b) // 10
  d = (minutes - 600 * a - 60 * b - 10 * c)

  time = ''
  for i in [a, b, c, d]:
    time += str(i)

  while time[0] == '0':
    time = time[1:]

  return time
  
ottawa = input().zfill(4)

minutes += int(ottawa[0]) * 600
minutes += int(ottawa[1]) * 60
minutes += int(ottawa[2]) * 10
minutes += int(ottawa[3])

print(converter(minutes), 'in Ottawa')
print(converter(minutes - 180), 'in Victoria')
print(converter(minutes - 120), 'in Edmonton')
print(converter(minutes - 60), 'in Winnipeg')
print(converter(minutes), 'in Toronto')
print(converter(minutes + 60), 'in Halifax')
print(converter(minutes + 90), "in St. John's")