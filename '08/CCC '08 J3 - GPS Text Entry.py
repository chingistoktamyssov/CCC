gps = {'A': [1, 1],'B': [2, 1],'C': [3, 1],'D': [4, 1],'E': [5, 1],'F': [6, 1],'G': [1, 2],'H': [2, 2],'I': [3, 2],'J': [4, 2],'K': [5, 2],'L': [6, 2],'M': [1, 3],'N': [2, 3],'O': [3, 3],'P': [4, 3],'Q': [5, 3],'R': [6, 3],'S': [1, 4],'T': [2, 4],'U': [3, 4],'V': [4, 4],'W': [5, 4],'X': [6, 4],'Y': [1, 5],'Z': [2, 5],' ': [3, 5],'-': [4, 5],'.': [5, 5], '1': [6, 5]}
position = [1, 1]
steps = 0

word = input()
word += '1'

for i in word:
  steps += abs(position[0] - gps[i][0]) + abs(position[1] - gps[i][1])
  position = gps[i]

print(steps)