import bisect

docks = list(range(1, int(input())+1))

count = 0
x = True

for i in range(int(input())):
  plane = int(input())
  
  if x == True:
    pos = bisect.bisect_right(docks, plane) - 1
    
    if pos == -1:
      x = False
      
    else:
      docks.pop(pos)
      count += 1

print(count)