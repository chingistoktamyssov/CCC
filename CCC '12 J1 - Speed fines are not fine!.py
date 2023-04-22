limit = int(input())
speed = int(input())

if limit >= speed:
  print("Congratulations, you are within the speed limit!")
else:
  if 1 <= (speed - limit) <= 20:
    print("You are speeding and your fine is $100.")
  elif 21 <= (speed - limit) <= 30:
    print("You are speeding and your fine is $270.")
  elif 31 <= (speed - limit):
    print("You are speeding and your fine is $500.")
