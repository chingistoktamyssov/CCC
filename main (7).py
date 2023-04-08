import re

numbers = {1: 'A', 2: 'B', 3: 'C', 4: 'D', 5: 'E', 6: 'F', 7: 'G', 8: 'H', 9: 'I', 10: 'J', 11: 'K', 12: 'L', 13: 'M', 14: 'N', 15: 'O', 16: 'P', 17: 'Q', 18: 'R', 19: 'S', 20: 'T', 21: 'U', 22: 'V', 23: 'W', 24: 'X', 25: 'Y', 26: 'Z', 'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10, 'K': 11, 'L': 12, 'M': 13, 'N': 14, 'O': 15, 'P': 16, 'Q': 17, 'R': 18, 'S': 19, 'T': 20, 'U': 21, 'V': 22, 'W': 23, 'X': 24, 'Y': 25, 'Z': 26}

header = re.sub(r'\W+', '', input())
message = re.sub(r'\W+', '', input())

code = [[] for i in range(len(header))]

x = 0
stop = True
while stop:
  for i in range(len(header)):
    if x < len(message):
      code[i].append(message[x])
      x += 1
    else:
      stop = False
      break

shifted = [[] for i in range(len(header))]

for i in range(len(header)):
  for j in code[i]:
    if numbers[header[i]] - 1 + numbers[j] - 1 >= 26:
      shifted[i].append(numbers[numbers[header[i]] + numbers[j] - 27])
    else:
      shifted[i].append(numbers[numbers[header[i]] + numbers[j] - 1])

encryption = ''

x = 0
for i in range(len(header)):
  x += len(shifted[i])
x += len(header)

stop = True
while stop:
  for i in range(len(header)):
    encryption += shifted[i][0]
    shifted[i].pop(0)
    x -= 1
    if x <= len(header):
      stop = False
      break

print(encryption)