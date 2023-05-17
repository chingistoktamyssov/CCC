temp = 201

while 1:
  city = input().split()
  
  if temp == 201:
    temp = int(city[1])
    coolest = city[0]
  elif int(city[1]) < temp:
    temp = int(city[1])
    coolest = city[0]
    
  if city[0] == 'Waterloo':
    break

print(coolest)