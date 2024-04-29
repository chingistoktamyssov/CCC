import math

points = []
n=int(input())
for i in range(n):
    points.append([int(x) for x in input().split()])

biggest = -1

for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):

            x1, y1 = points[i]
            x2, y2 = points[j]
            x3, y3 = points[k]
            sides = []
            sides.append(math.sqrt((x1-x2)**2 + (y1-y2)**2))
            sides.append(math.sqrt((x1-x3)**2 + (y1-y3)**2))
            sides.append(math.sqrt((x2-x3)**2 + (y2-y3)**2))
            sides.sort()

            a, b, c = sides

            if a**2 + b**2 < c**2:
                biggest = max(biggest, c)
            else:
                semi = (a+b+c)/2
                area = math.sqrt(semi*(semi-a)*(semi-b)*(semi-c))

                if area == 0: continue
                    
                diameter = (a*b*c)/(4*area)*2
                biggest = max(biggest, diameter)
                
print("%.2f" % biggest)