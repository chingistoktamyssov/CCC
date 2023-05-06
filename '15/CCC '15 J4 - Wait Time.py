messages = []
for i in range(int(input())):
  messages.append(input().split())

friendtime = {}
friendstatus = {}

for i in range(len(messages)):
  if messages[i][0] == 'W':
    for j in friendtime:
      if friendstatus[j] == True:
        friendtime[j] += int(messages[i][1])
  else:
    if messages[i][0] == 'R':
      if messages[i][1] not in friendtime.keys():
        friendtime[messages[i][1]] = 0
      friendstatus[messages[i][1]] = True
    elif messages[i][0] == 'S':
      friendstatus[messages[i][1]] = False
    try:
      if messages[i + 1][0] != 'W':
        for j in friendtime:
          if friendstatus[j] == True:
            friendtime[j] += 1
    except:
      pass

for i in friendtime:
  if friendstatus[i] == True:
    friendtime[i] = -1

friendkeys = list(friendtime.keys())
friendkeys.sort()
friendtime = {i: friendtime[i] for i in friendkeys}

for i in friendtime:
  print(i, friendtime[i])
