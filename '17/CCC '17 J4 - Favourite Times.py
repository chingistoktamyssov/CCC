after = int(input())
counter = 0

counter += 31 * (after // 720)
after -= 720 * (after // 720)

def minutestotime(minutes):
    
  time = ''

  if minutes > 720:
    minutes %= 720
    if 0 <= minutes <= 59:
      minutes += 720
  
  h1 = minutes // 600
  h2 = (minutes - h1 * 600) // 60
  m1 = (minutes - h1 * 600 - h2 * 60) // 10
  m2 = (minutes - h1 * 600 - h2 * 60 - m1 * 10)

  time = str(h1) + str(h2) + str(m1) + str(m2)

  return time

for i in range(720, 720 + after + 1):
  time = minutestotime(i)

  if time[0] == '0':
    time = time[1:]
    if int(time[1]) - int(time[0]) == int(time[2]) - int(time[1]):
      counter += 1
  else:
    if int(time[1]) - int(time[0]) == int(time[2]) - int(time[1]) == int(time[3]) - int(time[2]):
      counter += 1

print(counter)