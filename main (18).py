while True:
  word = input()
  if word == 'X':
    break
  while True:
    if 'ANA' in word:
      word = word.replace('ANA', 'A')
    elif 'BAS' in word:
      word = word.replace('BAS', 'A')
    else:
      break
  if word == 'A':
    print('YES')
  else:
    print('NO')