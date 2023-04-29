letters = 'ABCDEFGHIJKLMNOPQRST'
digits = '0123456789'

fix = input() + 'Z'

digitlook = False
word = ''

for i in fix:

  if i == 'Z':
    print(word)
  
  elif digitlook == True:
    if i in digits:
      word += i
    else:
      print(word)
      word = i
      digitlook = False
      
  elif i in letters:
    word += i
    
  else:
    if i == '+':
      word += ' tighten '
    elif i == '-':
      word += ' loosen '
    digitlook = True