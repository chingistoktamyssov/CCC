t = input()
s = input()
cyclic = True

for i in range(len(s)):
  s += s[0]
  s = s[1:]
  shift = ''.join(str(j) for j in s)
  if shift in t:
    print("yes")
    cyclic = False
    break

if cyclic:
  print("no")
