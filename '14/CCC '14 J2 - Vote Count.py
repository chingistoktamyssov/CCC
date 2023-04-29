a = int(input())

vote = input()
letter = [x for x in vote]

if letter.count('A') > letter.count('B'):
  print("A")
elif letter.count('B') > letter.count('A'):
  print("B")
elif letter.count('A') == letter.count('B'):
  print("Tie")
