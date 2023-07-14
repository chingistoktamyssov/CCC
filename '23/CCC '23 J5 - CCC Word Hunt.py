w = input()
r, c = int(input()), int(input())

puzzle = []
for i in range(r):
  puzzle.append(input().split())

def inbound(x, y):
  if 0 <= x <= r - 1 and 0 <= y <= c-1:
    return True
  return False

found = 0
def solve(x, y, d, n, t):

  global found
  
  if n == 1:
    if inbound(x + 1, y) and puzzle[x + 1][y] == w[n]:
      solve(x + 1, y, 'down', n+1, t)
    if inbound(x - 1, y) and puzzle[x - 1][y] == w[n]:
      solve(x - 1, y, 'up', n+1, t)
    if inbound(x, y + 1) and puzzle[x][y + 1] == w[n]:
      solve(x, y + 1, 'right', n+1, t)
    if inbound(x, y - 1) and puzzle[x][y - 1] == w[n]:
      solve(x, y - 1, 'left', n+1, t)
    if inbound(x + 1, y + 1) and puzzle[x + 1][y + 1] == w[n]:
      solve(x + 1, y + 1, 'downright', n+1, t)
    if inbound(x - 1, y - 1) and puzzle[x - 1][y - 1] == w[n]:
      solve(x - 1, y - 1, 'upleft', n+1, t)
    if inbound(x + 1, y - 1) and puzzle[x + 1][y - 1] == w[n]:
      solve(x + 1, y - 1, 'downleft', n+1, t)
    if inbound(x - 1, y + 1) and puzzle[x - 1][y + 1] == w[n]:
      solve(x - 1, y + 1, 'upright', n+1, t)
  elif n == len(w):
    found += 1
  else:
    if d == 'down':
      if inbound(x + 1, y) and puzzle[x + 1][y] == w[n]:
        solve(x + 1, y, 'down', n+1, t)
      if t == 0:
        if inbound(x, y - 1) and puzzle[x][y - 1] == w[n]:
          solve(x, y - 1, 'left', n+1, t+1)
        if inbound(x, y + 1) and puzzle[x][y + 1] == w[n]:
          solve(x, y + 1, 'right', n+1, t+1)
    if d == 'up':
      if inbound(x - 1, y) and puzzle[x - 1][y] == w[n]:
        solve(x - 1, y, 'up', n+1, t)
      if  t == 0:
        if inbound(x, y - 1) and puzzle[x][y - 1] == w[n]:
          solve(x, y - 1, 'left', n+1, t+1)
        if inbound(x, y + 1) and puzzle[x][y + 1] == w[n]:
          solve(x, y + 1, 'right', n+1, t+1)
    if d == 'right':
      if inbound(x, y + 1) and puzzle[x][y + 1] == w[n]:
        solve(x, y + 1, 'right', n+1, t)
      if t == 0:
        if inbound(x - 1, y) and puzzle[x - 1][y] == w[n]:
          solve(x - 1, y, 'up', n+1, t+1)
        if inbound(x + 1, y) and puzzle[x + 1][y] == w[n]:
          solve(x + 1, y, 'down', n+1, t+1)
    if d == 'left':
      if inbound(x, y - 1) and puzzle[x][y - 1] == w[n]:
        solve(x, y - 1, 'left', n+1, t)
      if t == 0:
        if inbound(x - 1, y) and puzzle[x - 1][y] == w[n]:
          solve(x - 1, y, 'up', n+1, t+1)
        if inbound(x + 1, y) and puzzle[x + 1][y] == w[n]:
          solve(x + 1, y, 'down', n+1, t+1)
    if d == 'downright':
      if inbound(x + 1, y + 1) and puzzle[x + 1][y + 1] == w[n]:
        solve(x + 1, y + 1, 'downright', n+1, t)
      if t == 0:
        if inbound(x + 1, y - 1) and puzzle[x + 1][y - 1] == w[n]:
          solve(x + 1, y - 1, 'downleft', n+1, t+1)
        if inbound(x - 1, y + 1) and puzzle[x - 1][y + 1] == w[n]:
          solve(x - 1, y + 1, 'upright', n+1, t+1)
    if d == 'upleft':
      if inbound(x - 1, y - 1) and puzzle[x - 1][y - 1] == w[n]:
        solve(x - 1, y - 1, 'upleft', n+1, t)
      if t == 0:
        if inbound(x + 1, y - 1) and puzzle[x + 1][y - 1] == w[n]:
          solve(x + 1, y - 1, 'downleft', n+1, t+1)
        if inbound(x - 1, y + 1) and puzzle[x - 1][y + 1] == w[n]:
          solve(x - 1, y + 1, 'upright', n+1, t+1)
    if d == 'downleft':
      if inbound(x + 1, y - 1) and puzzle[x + 1][y - 1] == w[n]:
        solve(x + 1, y - 1, 'downleft', n+1, t)
      if t == 0:
        if inbound(x - 1, y - 1) and puzzle[x - 1][y - 1] == w[n]:
          solve(x - 1, y - 1, 'upleft', n+1, t+1)
        if inbound(x + 1, y + 1) and puzzle[x + 1][y + 1] == w[n]:
          solve(x + 1, y + 1, 'downright', n+1, t+1)
    if d == 'upright':
      if inbound(x - 1, y + 1) and puzzle[x - 1][y + 1] == w[n]:
        solve(x - 1, y + 1, 'upright', n+1, t)
      if t == 0:
        if inbound(x - 1, y - 1) and puzzle[x - 1][y - 1] == w[n]:
          solve(x - 1, y - 1, 'upleft', n+1, t+1)
        if inbound(x + 1, y + 1) and puzzle[x + 1][y + 1] == w[n]:
          solve(x + 1, y + 1, 'downright', n+1, t+1)
      
for i in range(len(puzzle)):
  for j in range(len(puzzle[i])):
    if puzzle[i][j] == w[0]:
      solve(i, j, 'notfound', 1, 0)

print(found)