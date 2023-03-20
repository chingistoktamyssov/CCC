hand = input()

val = []
names = ['Clubs ', 'Diamonds ', 'Hearts ', 'Spades ']
total = 0

hand = hand.replace('C', 'X')
hand = hand.replace('D', 'X')
hand = hand.replace('H', 'X')
hand = hand.replace('S', 'X')
hand = hand.split('X', 4)
hand.pop(0)

for i in range(4):
  if len(hand[i]) == 0:
    x = 3
  elif len(hand[i]) == 1:
    x = 2
  elif len(hand[i]) == 2:
    x = 1
  else:
    x = 0
  val.append(hand[i].count('A') * 4 + hand[i].count('K') * 3 + hand[i].count('Q') * 2 + hand[i].count('J') + x)

print('Cards Dealt                       Points')

for i in range(4):
  print(str(names[i]) + ' '.join(hand[i]) + str(' ' * (40 - len(str(val[i])) - len(str(names[i])) - len(' '.join(hand[i])))) + str(val[i]))
for x in val:
  total = total + x
  
print(' ' * (40 - 6 - len(str(total))) + 'Total ' + str(total))