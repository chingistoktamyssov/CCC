n = int(input())

if n == 0:
  pass

elif n == 1:
  computer = input().split()
  print(computer[0])

else:
  
  for i in range(n):
    
    computer = input().split()
    total = 2 * int(computer[1]) + 3 * int(computer[2]) + int(computer[3])
    
    if i == 0:
      first = [computer[0], total]
      
    elif i == 1:
      if total > first[1]:
        first, second = [computer[0], total], first
      elif total < first[1]:
        second = [computer[0], total]
      else:
        if min(first[0], computer[0]) == first[0]:
          second = [computer[0], total]
        else:
          first, second = [computer[0], total], first
          
    else:
      if total > first[1]:
        first, second = [computer[0], total], first
      elif total == first[1]:
        if min(first[0], computer[0]) == first[0]:
          second = [computer[0], total]
        else:
          first, second = [computer[0], total], first
      elif first[1] > total > second[1]:
        second = [computer[0], total]
      elif total == second[1]:
        if min(second[0], computer[0]) == computer[0]:
          second = [computer[0], total]

  print(first[0])
  print(second[0])