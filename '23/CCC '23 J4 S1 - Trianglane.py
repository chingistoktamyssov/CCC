n = int(input())
row1 = [int(x) for x in input().split()] + [0]
row2 = [int(x) for x in input().split()] + [0]
k = 0

for i in range(n):
  if row1[i] == 1:
    k+=3
    if row1[i+1] == 1:
      k-=2
      
for i in range(n):
  if row2[i] == 1:
    k+=3
    if row2[i+1] == 1:
      k-=2
    if i % 2 == 0:
      if row1[i] == 1:
        k-=2
        
print(k)