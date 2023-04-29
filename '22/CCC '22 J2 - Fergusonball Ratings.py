players = int(input())
stars = 0

for i in range(players):
  rating = int(input()) * 5 - int(input()) * 3
  
  if rating > 40:
    stars += 1

if stars == players:
  print(str(stars) + '+')
else:
  print(stars)