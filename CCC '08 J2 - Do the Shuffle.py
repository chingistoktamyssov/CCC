playlist = ['A', 'B', 'C', 'D', 'E']

while 1:
  b = int(input())
  n = int(input())

  if b == 4 and n == 1:
    break

  for i in range(n):
    if b == 1:
      x = playlist.copy()[0]
      playlist.pop(0)
      playlist.insert(4, x)

    elif b == 2:
      x = playlist.copy()[-1]
      playlist.pop(-1)
      playlist.insert(0, x)

    elif b == 3:
      playlist[0], playlist[1] = playlist[1], playlist[0]

print(' '.join(playlist))
