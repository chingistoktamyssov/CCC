for i in range(int(input())):
  w1 = input()
  w2 = input()
  w3 = input()
  
  found = False

  if found == False:
    try:
      if w1 == w2[:len(w1)]:
        print('No')
        found = True
    except:
      pass
      
  if found == False:
    try:
      if w1 == w3[:len(w1)]:
        print('No')
        found = True
    except:
      pass
      
  if found == False:
    try:
      if w2 == w1[:len(w2)]:
        print('No')
        found = True
    except:
      pass
      
  if found == False:
    try:
      if w2 == w3[:len(w2)]:
        print('No')
        found = True
    except:
      pass
      
  if found == False:
    try:
      if w3 == w1[:len(w3)]:
        print('No')
        found = True
    except:
      pass
      
  if found == False:
    try:
      if w3 == w2[:len(w3)]:
        print('No')
        found = True
    except:
      pass

  if found == False:
    try:
      if w1 == w2[-len(w1):]:
        print('No')
        found = True
    except:
      pass
      
  if found == False:
    try:
      if w1 == w3[-len(w1):]:
        print('No')
        found = True
    except:
      pass
      
  if found == False:
    try:
      if w2 == w1[-len(w2):]:
        print('No')
        found = True
    except:
      pass
      
  if found == False:
    try:
      if w2 == w3[-len(w2):]:
        print('No')
        found = True
    except:
      pass
      
  if found == False:
    try:
      if w3 == w1[-len(w3):]:
        print('No')
        found = True
    except:
      pass
      
  if found == False:
    try:
      if w3 == w2[-len(w3):]:
        print('No')
        found = True
    except:
      pass
      
  if found == False:
    print('Yes')