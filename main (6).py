n = int(input())
m = int(input())

adjectives = []
nouns = []

for i in range(n):
  adjectives.append(input())
for i in range(m):
  nouns.append(input())

for i in range(n):
  for j in range(m):
    print(str(adjectives[i]) + " as " + str(nouns[j]))