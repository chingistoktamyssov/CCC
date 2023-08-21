to_index = {'A':0,'B':1,'C':2,'D':3,'E':4,'F':5,'G':6,'H':7,'I':8,'J':9, '1':0,'2':1,'3':2,'4':3,'5':4,'6':5,'7':6,'8':7,'9':8}

graph = []
for i in range(10):
  graph.append(input().split()) 

def cell_finder(cell, count):
  if count >= 100:
    return '*'
  elif graph[cell[0]][cell[1]].isnumeric():
    return graph[cell[0]][cell[1]]
  else:
    sum = 0
    count += 1
    for i in graph[cell[0]][cell[1]].split('+'):
      part = cell_finder([to_index[i[0]],to_index[i[1]]], count)
      part = str(part)
      if part.isnumeric():
        sum += int(part)
      else:
        return '*'
    graph[cell[0]][cell[1]] = str(sum)
    return sum
    
spreadsheet = []
for i in range(len(graph)):
  row = []
  for j in range(len(graph[i])):
    row.append(str(cell_finder([i, j], 0)))
  spreadsheet.append(row)

for row in spreadsheet:
  print(' '.join(row))