book = {}
visitable = [1]
queue = [1]
count = 1
x = True

n = int(input())

for i in range(1, n+1):
  page = input()
  
  if page == '0':
    book[i] = 0
    
  else:
    paths = [int(x) for x in page.split()]
    book[i] = paths[1:]

    for j in paths[1:]:
      if j != i:
        visitable.append(j)

if len(set(visitable)) == n:
    print("Y")
else:   
    print("N")

while len(queue) > 0 and x == True:
  
  for i in range(len(queue)):
    if x == False:
      break

    for j in book[queue[0]]:
      if book[j] == 0:
        print(count+1)
        x = False
        break
        
      else:
        queue.append(j)
    queue.pop(0)

  count += 1

if x == True:
  print(count)