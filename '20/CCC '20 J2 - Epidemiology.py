p,n,r = int(input()),int(input()),int(input())
day = 0
infected = n

while infected <= p:
  infected += n * r
  n *= r
  day += 1

print(day)