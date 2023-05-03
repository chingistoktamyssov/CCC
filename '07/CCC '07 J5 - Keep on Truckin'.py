motels = [
  0, 990, 1010, 1970, 2030, 2940, 3060, 3930, 4060, 4970, 5030, 5990, 6010,
  7000
]

min, max = int(input()), int(input())

for i in range(int(input())):
  motels.append(int(input()))

paths = [0] * len(motels)
paths[0] = 1

motels.sort()

for i in range(len(motels)):
  for j in range(len(motels)):
    for k in range(min, max+1):
      if motels[i] + k == motels[j]:
        paths[j] += paths[i]

print(paths[-1])