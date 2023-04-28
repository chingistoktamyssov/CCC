directions = []
x = -1

while 1:
  instruction = input()
  if instruction == '99999':
    break

  sum = int(instruction[0]) + int(instruction[1])
  
  if sum % 2 == 1:
    print('left', instruction[2:5])
    directions.append('left')
  elif sum % 2 == 0 and sum != 0:
    print('right', instruction[2:5])
    directions.append('right')
  else:
    print(directions[x], instruction[2:5])
    directions.append(directions[x])

  x += 1