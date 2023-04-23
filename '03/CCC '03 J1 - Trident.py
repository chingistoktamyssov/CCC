t = int(input())
a = int(input())
h = int(input())

for i in range(t):
  print('*' + ' ' * a + '*' + ' ' * a + '*')

print('*' * 2 * a + '*' * 3)

for i in range(h):
  print(' ' + ' ' * a + '*')
