for i in range(int(input())):

  word = input()
  compress = ''
  count = 0
  
  for i in range(len(word)):
    if i == 0:
      old = word[i]
      count += 1
    else:
      if word[i] == old:
        count += 1
      else:
        compress += str(count) + ' ' + str(old) + ' '
        old = word[i]
        count = 1
        
    if i + 1 == len(word):
      compress += str(count) + ' ' + str(old) + ' '
      
  print(compress)