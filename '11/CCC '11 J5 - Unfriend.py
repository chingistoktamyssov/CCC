from itertools import combinations

friends = {}
people = []
removablesets = 0

for i in range(int(input()) - 1):
  friends[i+1] = int(input())
  people.append(i+1)

invites = []
for i in friends.values():
  invites.append(i)

def toremove(tryremove):
  occurences = []
  for i in tryremove:
    for j in range(len(invites)):
      if i == invites[j]:
        occurences.append(j+1)

  for i in occurences:
    if i not in tryremove:
      return 0
  return 1

peoplecombos = []

for i in range(len(people) + 1):
  peoplecombos += list(combinations(people, i))

for i in peoplecombos:
  removablesets += toremove(i)
  
print(removablesets)