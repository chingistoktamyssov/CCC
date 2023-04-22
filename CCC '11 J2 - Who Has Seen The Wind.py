h = int(input())
m = int(input())

b = True

for i in range(m):
  a = (-6 * (i+1)**4) + (h * (i+1)**3) + (2 * (i+1)**2) + (i+1)
  if a <= 0:
    b = False
    break
  else:
    pass
    
if b == False:
  print('The balloon first touches ground at hour:')
  print(i+1)
  
else:
  print('The balloon does not touch ground in the given time.')
