n = int(input())
o1 = input().split()
o2 = input().split()

pairings = {}
bad = False

for i in range(n):
  if o1[i] == o2[i]:
    bad = True
    break
  elif o1[i] not in pairings:
    pairings[o2[i]] = o1[i]
  else:
    if o2[i] != pairings[o1[i]]:
      bad = True
      break

if bad == False:
  print('good')
else:
  print('bad')