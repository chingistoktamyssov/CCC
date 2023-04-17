todo = [(1, 7), (1, 4), (2, 1), (3, 4), (3, 5)]
tasks = {1, 2, 3, 4, 5, 6, 7}
travelled = []
possible = True

while True:
  x, y = int(input()), int(input())
  if x == 0 and y == 0:
    break
  todo.append((x, y))

def queuemaker(todo, travelled):
  nonoptions = []
  for i in todo:
    nonoptions.append(i[1])
  nonoptions.extend(travelled)
  nonoptions = set(nonoptions)
  queue = []
  for i in tasks.difference(nonoptions):
    queue.append(i)
  queue.sort()
  return queue

queue = queuemaker(todo, travelled)

while len(todo) != 0:
  travelled.append(queue[0])
  toremove = []
  for i in range(len(todo)):
    if todo[i][0] == queue[0]:
      toremove.append(i)  
  x = 0
  for i in toremove:
    todo.pop(i - x)
    x += 1 
  queue.pop(0)
  queue = queuemaker(todo, travelled)
  if len(queue) == 0:
    possible = False
    break

if possible == False:
  print('Cannot complete these tasks. Going to bed.')
else:
  for i in queue:
    travelled.append(i)
  travelledstr = ''
  for i in travelled:
    travelledstr += str(i)
  print(' '.join(travelledstr))