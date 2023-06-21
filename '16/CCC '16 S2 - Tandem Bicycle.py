question = int(input())
n = int(input())
c1 = sorted([int(x) for x in input().split()])
c2 = sorted([int(x) for x in input().split()])

total = 0

if question == 1:
  for i in range(n):
    speed = max(c1[i], c2[i])
    total += speed

else:
  for i in range(n):
    speed = max(c1[i], c2[-(i+1)])
    total += speed

print(total)