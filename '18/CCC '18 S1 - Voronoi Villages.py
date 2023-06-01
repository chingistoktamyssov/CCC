villages = []
for i in range(int(input())):
  villages.append(int(input()))
villages.sort()

smallsum = (villages[1] - villages[0])/2 + (villages[2] - villages[1])/2

for i in range(len(villages)):
  if 0 < i < len(villages)-1:
    sum = (villages[i] - villages[i-1])/2 + (villages[i+1] - villages[i])/2
    if sum < smallsum:
      smallsum = sum

print(smallsum)