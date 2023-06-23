n = int(input())
tides = sorted([int(x) for x in input().split()])

order = []

if n % 2 == 1:
  lows = tides[0:n//2+1]
  lows.reverse()
  highs = tides[n//2+1:n]
  
  for i in range(n//2):
    order.append(lows[i])
    order.append(highs[i])

  order.append(lows[-1])
  
else:
  lows = tides[0:n//2]
  lows.reverse()
  highs = tides[n//2:n]

  for i in range(n//2):
    order.append(lows[i])
    order.append(highs[i])

print(' '.join(str(x) for x in order))