xj, yj, xr, yr = [int(x) for x in input().split()]
small_x, big_x, small_y, big_y = min(xj, xr), max(xj, xr), min(yj, yr), max(yj, yr)

if xj == xr:
    lineType = 'vertical'
elif yj == yr:
    lineType = 'horizontal'
else:
    lineType = 'slope'
    m = (yr-yj)/(xr-xj)
    b = yj-xj*m

count = 0
n = int(input())
for i in range(n):
    
    building = [int(x) for x in input().split()]
    corners = building[0]
    
    j = 1
    
    for k in range(corners):
        x1, y1 = building[j], building[j+1]
        if j == corners*2-1: 
            x2, y2 = building[1], building[2]
        else: 
            x2, y2 = building[j+2], building[j+3]
        smalltemp_x, bigtemp_x, smalltemp_y, bigtemp_y = min(x1, x2), max(x1, x2), min(y1, y2), max(y1, y2)
    
        j += 2
        
        if x1 == x2:    
            line2Type = 'vertical'
        elif y1 == y2:
            line2Type = 'horizontal'
        else:
            line2Type = 'slope'
            mtemp = (y2-y1)/(x2-x1)
            btemp = y1-x1*mtemp
        
        if lineType == 'vertical':
            if line2Type == 'vertical':
                if xj == x1:
                    if small_y <= y1 <= big_y or small_y <= y2 <= big_y:
                        count += 1
                        break
            elif line2Type == 'horizontal':
                if small_y <= y1 <= big_y and smalltemp_x <= xj <= bigtemp_x:
                    count += 1
                    break
            else:
                if small_y <= mtemp*xj+btemp <= big_y and smalltemp_x <= xj <= bigtemp_x:
                    count += 1
                    break

        elif lineType == 'horizontal':
            if line2Type == 'vertical':
                if small_x <= x1 <= big_x and smalltemp_y <= yj <= bigtemp_y:
                    count += 1
                    break
            elif line2Type == 'horizontal':
                if yj == y1:
                    if small_x <= x1 <= big_x or small_x <= x2 <= big_x:
                        count += 1
                        break
            else:
                if small_x <= (yj - btemp) / mtemp <= big_x and smalltemp_y <= yj <= bigtemp_y:
                    count += 1
                    break
                
        else:
            if line2Type == 'vertical':
                if smalltemp_y <= m*x1+b <= bigtemp_y:
                    count += 1
                    break
            elif line2Type == 'horizontal':
                if smalltemp_x <= (y1 - b) / m <= bigtemp_x:
  
                    count += 1
                    break
            else:  
                if m == mtemp:
                    if b == btemp:
                        if small_x <= x1 <= big_x or small_x <= x2 <= big_x:
                      
                            count += 1
                            break
                else:
                    xintersection = (b-btemp) / (mtemp-m)
                    if small_x <= xintersection <= big_x and smalltemp_y <= xintersection*mtemp+btemp<=bigtemp_y:
                        count += 1
                        break
print(count)