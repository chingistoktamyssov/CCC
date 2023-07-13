wins = 0

games = [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]
points = [0, 0, 0, 0]

t, g = int(input()), int(input())

for i in range(g):
  result = [int(x) for x in input().split()]
  games.remove([result[0], result[1]])
  
  if result[2] > result[3]:
    points[result[0]-1] += 3
  elif result[3] > result[2]:
    points[result[1]-1] += 3
  else:
    points[result[0]-1] += 1
    points[result[1]-1] += 1
    
reset = []
for i in points:
  reset.append(i)

def countwin(n, results):
  global wins

  if n == len(games):
    
    for i in range(len(results)):
      if results[i] == 'w':
        points[int(results[i+1])-1] += 3
      elif results[i] == 't':
        points[int(results[i+1])-1] += 1
        points[int(results[i+2])-1] += 1

    x = True
    for i in range(len(points)):
      if i != t-1 and points[i] >= points[t-1]:
        x = False
    if x == True:
      wins += 1
      
    points.clear()
    for i in reset:
      points.append(i)

  else:

    for i in [[n+1, results + 'w' + str(games[n][0])], [n+1, results + 'w' + str(games[n][1])], [n+1, results + 't' + str(games[n][0]) + str(games[n][1])]]:
      countwin(i[0], i[1])

countwin(0, '')
print(wins)