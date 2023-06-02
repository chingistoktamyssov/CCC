observations = []
for i in range(int(input())):
  speed = [int(x) for x in input().split()]
  observations.append(speed)

def first(x):
  return x[0]

observations.sort(key=first)

maxspeed = 0
for i in range(len(observations)):
  if i != len(observations)-1:
    speed = abs(observations[i+1][1] - observations[i][1]) / (observations[i+1][0] - observations[i][0])
    
    if speed > maxspeed:
      maxspeed = speed

print(maxspeed)