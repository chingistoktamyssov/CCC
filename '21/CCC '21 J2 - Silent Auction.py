names = []
bets = []

for i in range(int(input())):
  names.append(input())
  bets.append(int(input()))

print(names[bets.index(max(bets))])