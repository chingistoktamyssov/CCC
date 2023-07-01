roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

total = 0
number = input()

while 1:
  if len(number) <= 2:
    total += (int(number[0]) * roman[number[1]])
    break
  else:
    if roman[number[1]] < roman[number[3]]:
      total -= (int(number[0]) * roman[number[1]])
    else:
      total += (int(number[0]) * roman[number[1]])
    number = number[2:]

print(total)