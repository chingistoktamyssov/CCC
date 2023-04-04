vowels = ['A', 'a', 'E', 'e', 'I', 'i', 'O', 'o', 'U', 'u']

n = int(input())

for i in range(n):
  endline = []

  for j in range(4):
    syllable = False
    endword = ''
    
    line = input().split()
    word = line[-1][::-1]

    for x in range(len(word)):
      if word[x] in vowels:
        endword += word[:x+1][::-1]
        syllable = True
        break

    if syllable == False:
      endword += line[-1]
    endline.append(endword)

  for i in range(4):
    endline[i] = endline[i].lower()

  if endline[0] == endline[1] == endline[2] == endline[3]:
    print('perfect')
  elif endline[0] == endline[1] and endline[2] == endline[3]:
    print('even')
  elif endline[0] == endline[2] and endline[1] == endline[3]:
    print('cross')
  elif endline[0] == endline[3] and endline[1] == endline[2]:
    print('shell')
  else:
    print('free')