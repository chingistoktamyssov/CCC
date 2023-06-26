plain = input()
code = input()

translate = {}
for i in range(len(plain)):
  translate[code[i]] = plain[i]
  
decode = input()

message = ''
for i in decode:
  try:
    message += translate[i]
  except:
    message += '.'

print(message)