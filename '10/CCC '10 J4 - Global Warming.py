n = [int(x) for x in input().split()]

while n[0] != 0:
  
  if len(n) == 2:
    print(0)
    
  else:
    d = []
    n.pop(0)
    for i in range(len(n)-1):
      d.append(n[i+1] - n[i])
      
    for i in range(len(d)):
      y = True
      x = [d[a:a+i+1] for a in range(0, len(d), i+1)]
      for j in range(len(x)-1):
        if x[j] == x[j+1]:
          pass
        else:
          if x[j][slice(len(x[j+1]))] == x[j+1]:
            pass
          else:
            y = False
            
      if y == True:
        print(i+1)
        break
      else:
        pass
        
  n = [int(x) for x in input().split()]