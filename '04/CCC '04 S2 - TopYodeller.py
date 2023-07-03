n, k = [int(x) for x in input().split()]

scores = {}
worst = {}
for i in range(n):
  scores[i+1] = 0
  worst[i+1] = 0

for i in range(k):
  round = [int(x) for x in input().split()]

  ranks = {}
  for j in range(n):
    scores[j+1] += round[j]
    if scores[j+1] in ranks:
      ranks[scores[j+1]].append(j+1)
    else:
      ranks[scores[j+1]] = [j+1]
  ranks = sorted(ranks.items(), reverse=True)

  assign = 1
  for j in ranks:
    for k in j[1]:
      if assign > worst[k]:
        worst[k] = assign
    assign += 1

topscore = scores[1]
yodeller = []
for i in scores:
  if scores[i] > topscore:
    topscore = scores[i]
    yodeller = [i]
  elif scores[i] == topscore:
    yodeller.append(i)

yodeller.sort()
for i in yodeller:
  print('Yodeller ' + str(i) + ' is the TopYodeller: score ' + str(scores[i]) + ', worst rank ' + str(worst[i]))