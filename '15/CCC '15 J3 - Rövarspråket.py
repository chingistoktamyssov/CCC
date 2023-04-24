numbers = {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e', 6: 'f', 7: 'g', 8: 'h', 9: 'i', 10: 'j', 11: 'k', 12: 'l', 13: 'm', 14: 'n', 15: 'o', 16: 'p', 17: 'q', 18: 'r', 19: 's', 20: 't', 21: 'u', 22: 'v', 23: 'w', 24: 'x', 25: 'y', 26: 'z', 'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26}

vowels = ('a', 'e', 'i', 'o', 'u')

english = input()
swedish = ''

def vowelfinder(consonant):
  
  vowelno = False
  n1 = numbers[consonant]
  n2 = numbers[consonant]
  
  while numbers[n1] not in vowels:
    n1 -= 1
  while numbers[n2] not in vowels:
    n2 += 1
    try:
      numbers[n2]
    except:
      vowelno = True
      break
      
  if vowelno == True:
    return numbers[n1]
    
  else:
    diff1 = abs(numbers[consonant] - n1)
    diff2 = abs(numbers[consonant] - n2)
  
    if diff1 < diff2:
      return numbers[n1]
    elif diff2 < diff1:
      return numbers[n2]
    else:
      return numbers[n1]

def consonantfinder(consonant):
  if consonant == 'z':
    return 'z'
    
  else:
    n = numbers[consonant] + 1

    while numbers[n] in vowels:
      n += 1

  return numbers[n]

for i in english:
  if i in vowels:
    swedish += i
  else:
    swedish += i + vowelfinder(i) + consonantfinder(i)

print(swedish)