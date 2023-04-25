time = input()
distance = 0

minutes = int(time[0]) * 600 + int(time[1]) * 60 + int(time[3]) * 10 + int(time[4])

while distance < 1:
  
  if 420 <= minutes <= 600:
    distance += 1/240
  elif 900 <= minutes <= 1140:
    distance += 1/240
  else:
    distance += 1/120

  minutes += 1
  
  if minutes == 1440:
    minutes = 0

minutes -= 1

h1 = minutes // 600
h2 = (minutes - h1 * 600) // 60
m1 = (minutes - h1 * 600 - h2 * 60) // 10
m2 = (minutes - h1 * 600 - h2 * 60 - m1 * 10)

print(str(h1) + str(h2) + ':' + str(m1) + str(m2))