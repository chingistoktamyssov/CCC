n = int(input())
y = input()
t = input()
listy = []
listt = []
a = 0

listy = [x for x in y]
listt = [x for x in t]

for i in range(n):
 if listy[i] == listt[i] == 'C':
   a = a + 1
 else:
   pass

print(a)