grid = [1, 2 , 3, 4]
n = list(input())

for i in n:
  if i == 'H':
    grid[0], grid[2] = grid[2], grid[0]
    grid[1], grid[3] = grid[3], grid[1]
  elif i == 'V':
    grid[0], grid[1] = grid[1], grid[0]
    grid[2], grid[3] = grid[3], grid[2]

print(grid[0], grid[1])
print(grid[2], grid[3])