sign = ['WELCOME', 'TO', 'CCC', 'GOOD', 'LUCK', 'TODAY']
lines = ['']
periods = [[]]

x = 0

w = int(input())

for i in sign:
  if len(lines[x]) == 0:
    lines[x] += i
  elif len(lines[x]) + len(i) + 1 <= w:
    lines[x] += '.' + i
  else:
    lines.append('')
    x += 1
    lines[x] += i

x = 0

for i in lines:
  for j in range(len(i)):
    if i[j] == '.':
      periods[x].append(j)
  periods.append([])
  x += 1
periods.pop()

for i in range(len(periods)):
  while len(lines[i]) != w:
    if len(periods[i]) == 0:
      lines[i] += '.' * (w - len(lines[i]))
      break
    
    for j in periods[i]:
      lines[i] = lines[i][:j] + '.' + lines[i][j:]
      for q in range(len(periods[i])):
        periods[i][q] += 1
      if len(lines[i]) == w:
        break

for i in lines:
  print(i)