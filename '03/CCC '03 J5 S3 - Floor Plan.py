flooring = int(input())
r, c = int(input()), int(input())

plan = [' ' * (c+2)]
for i in range(r):
    plan.append(' ' + input() + ' ')
plan.append(' ' * (c+2))

toexplore = []
explored = []
rooms = []
count = 0
roomsize = []

for i in range(1, r+1):
    for j in range(1, c+1):
        if plan[i][j] == '.' and [i, j] not in explored:
            toexplore.append([i, j])
            while len(toexplore) > 0:
              
                explored.append(toexplore[0])
             
                if plan[toexplore[0][0]-1][toexplore[0][1]] == '.' and [toexplore[0][0]-1, toexplore[0][1]] not in explored and [toexplore[0][0]-1, toexplore[0][1]] not in toexplore:
                  toexplore.append([toexplore[0][0]-1, toexplore[0][1]])
                if plan[toexplore[0][0]][toexplore[0][1]+1] == '.' and [toexplore[0][0], toexplore[0][1]+1] not in explored and [toexplore[0][0], toexplore[0][1]+1] not in toexplore:
                    toexplore.append([toexplore[0][0], toexplore[0][1]+1])
                if plan[toexplore[0][0]+1][toexplore[0][1]] == '.' and [toexplore[0][0]+1,toexplore[0][1]] not in explored and [toexplore[0][0]+1,toexplore[0][1]] not in toexplore:
                    toexplore.append([toexplore[0][0]+1, toexplore[0][1]])
                if plan[toexplore[0][0]][toexplore[0][1]-1] == '.' and [toexplore[0][0],toexplore[0][1]-1] not in explored and [toexplore[0][0],toexplore[0][1]-1] not in toexplore:
                    toexplore.append([toexplore[0][0], toexplore[0][1]-1])

                toexplore.pop(0)
                count += 1
              
            roomsize.append(count)
            count = 0

roomsize.sort(reverse=True)

for i in roomsize:
    if flooring-i >= 0:
        flooring -= i
        count += 1
    else:
        break

if count == 1:
    print('1 room, ' + str(flooring) + ' square metre(s) left over')
else:
    print(str(count) + ' rooms, ' + str(flooring) + ' square metre(s) left over')