def within(x, y):
    if 0 <= x <= row-1 and 0 <= y <= column-1:
        return True
    return False

def solve(maze):

    queue = [[0, 0]]
    visited = [[0, 0]]
    count = 1
    
    if maze[row-1][column-1] == '*':
        return -1
  
    while queue:
        for i in range(len(queue)):

            node = queue.pop(0)

            if node == [row-1, column-1]:
                return count
            
            x, y = node

            if maze[x][y] == '+':
                if [x-1, y] not in visited and within(x-1, y):
                    queue.append([x-1, y])
                    visited.append([x-1, y])
                if [x+1, y] not in visited and within(x+1, y):
                    queue.append([x+1, y])
                    visited.append([x+1, y])
                if [x, y-1] not in visited and within(x, y-1):
                    queue.append([x, y-1])
                    visited.append([x, y-1])
                if [x, y+1] not in visited and within(x, y+1):
                    queue.append([x, y+1])
                    visited.append([x, y+1])
            if maze[x][y] == '-':
                if [x, y-1] not in visited and within(x, y-1):
                    queue.append([x, y-1])
                    visited.append([x, y-1])
                if [x, y+1] not in visited and within(x, y+1):
                    queue.append([x, y+1])
                    visited.append([x, y+1])
            if maze[x][y] == '|':
                if [x-1, y] not in visited and within(x-1, y):
                    queue.append([x-1, y])
                    visited.append([x-1, y])
                if [x+1, y] not in visited and within(x+1, y):
                    queue.append([x+1, y])
                    visited.append([x+1, y])
        count += 1

    return -1
    
for i in range(int(input())):
  
    row, column = int(input()), int(input())
    maze = []
    for i in range(row):
        maze.append(input())
    print(solve(maze))
