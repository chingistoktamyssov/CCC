def solve(n):
  if n == 1:
    return 0
  else:
    
    f2list = []
    for x in range(1, (n // 2) + 1):
      if (n - x) % x == 0: 
        f2list.append((n-x)//x)
        
    f2 = min(f2list)
    f1 = n // (f2 + 1)
    p = f1 * f2
    
    return f2 + solve(p)

n = int(input())

print(solve(n))