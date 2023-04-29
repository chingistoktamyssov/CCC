badsign = False
sign = []
goodwords = ['I', 'O', 'S', 'H', 'Z', 'X', 'N']

for i in input():
  sign.append(i)
  
for i in sign:
  if i in goodwords:
    pass
  else:
    badsign = True
    
if badsign == True:
  print("NO")
else:
  print("YES")