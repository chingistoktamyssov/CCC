phone = {
  'A': 2,
  'B': 2,
  'C': 2,
  'D': 3,
  'E': 3,
  'F': 3,
  'G': 4,
  'H': 4,
  'I': 4,
  'J': 5,
  'K': 5,
  'L': 5,
  'M': 6,
  'N': 6,
  'O': 6,
  'P': 7,
  'Q': 7,
  'R': 7,
  'S': 7,
  'T': 8,
  'U': 8,
  'V': 8,
  'W': 9,
  'X': 9,
  'Y': 9,
  'Z': 9
}
digits = '0123456789'

for i in range(int(input())):
  number = ''
  message = input()
  message = message.replace('-', '')
  message = message[:3] + '-' + message[3:6] + '-' + message[6:]

  for j in range(12):

    if message[j] in digits or message[j] == '-':
      number += message[j]

    else:
      number += str(phone[message[j]])

  print(number)