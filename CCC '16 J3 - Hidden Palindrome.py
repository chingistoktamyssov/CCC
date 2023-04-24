word = input()

counter = 0

for i in range(len(word)):
  for j in range(len(word) + 1):
    if word[0:j] == word[0:j][::-1]:
      if j > counter:
        counter = j
  word = word[1:]

print(counter)