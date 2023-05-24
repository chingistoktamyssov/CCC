t_total = 0
s_total = 0

n = int(input())

for i in range(n):
  snce = input()
  
  t = snce.count("t") + snce.count("T")
  s = snce.count("s") + snce.count("S")

  t_total += t
  s_total += s

if t_total > s_total:
  print("English")
elif s_total > t_total:
  print("French")
elif s_total == t_total:
  print("French")