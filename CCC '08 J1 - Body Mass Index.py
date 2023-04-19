weight, height = float(input()), float(input())

if 25 < (weight / height ** 2):
  print("Overweight")
elif 18.5 <= (weight / height ** 2) <= 25:
  print("Normal weight")
elif (weight / height ** 2) < 18.5:
  print("Underweight")
