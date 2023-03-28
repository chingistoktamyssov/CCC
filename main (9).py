consonants = ['b', 'c', 'd', 'f', 'g', 'j', 'k' , 'l', 'm' , 'n', 'p', 'q', 's', 't', 'v', 'x', 'z', 'h', 'r', 'w']
while True:
  word = input()
  if word == 'quit!':
    break
  a = ''
  if len(word) > 4:
    if word[-3] in consonants and word[-2] == 'o' and word[-1] == 'r':
      word = word[:-1] + 'u' + word[-1:]
  print(word)