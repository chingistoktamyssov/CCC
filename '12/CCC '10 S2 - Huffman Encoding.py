codes = {}

for i in range(int(input())):
  code = input().split()
  codes[code[1]] = code[0]

message = ''
section = ''

for i in input():
  section += i
  if section in codes:
    message += codes[section]
    section = ''

print(message)