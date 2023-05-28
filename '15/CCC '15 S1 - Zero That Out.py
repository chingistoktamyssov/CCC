import string
alphabet = string.ascii_lowercase

w1, w2 = input(), input()
l1, l2 = [], []

anagram = True

for i in alphabet:
  l1.append(w1.count(i))
  l2.append(w2.count(i))
asterix = w2.count('*')

for i in range(len(l1)):
  if l2[i] > l1[i]:
    print('N')
    anagram = False
    break
  elif l1[i] > l2[i]:
    asterix -= (l1[i] - l2[i])

if anagram == True:
  if asterix == 0:
    print('A')