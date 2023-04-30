a3 = int(input())
a2 = int(input())
a1 = int(input())

b3 = int(input())
b2 = int(input())
b1 = int(input())

atotal = a3 * 3 + a2 * 2 + a1 
btotal = b3 * 3 + b2 * 2 + b1

if atotal > btotal:
  print("A")
elif btotal > atotal:
  print("B")
elif atotal == btotal:
  print("T")