n = int(input())
friends = {}
for i in range(n):
  a, b = input().split()
  friends[a] = b
      
while 1:
  pair = input().split()
  if pair[0] == '0' and pair[1] == '0':
    break
    
  count = 0
  current = pair[0]
  found = False
  
  while count <= n:
    if friends[current] == pair[1]:
      print('Yes', count)
      found = True
      break
    else:
      current = friends[current]
      count += 1

  if found == False:
    print('No')