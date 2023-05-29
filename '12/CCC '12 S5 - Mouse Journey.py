brother = input().split()
r, c = int(brother[0]), int(brother[1])

dp = [[0 for i in range(c+1)] for j in range(r+1)]

for i in range(int(input())):
    cat = [int(i) for i in input().split()]

    if cat[0] == 1:
        for i in range(cat[1], c+1):
            dp[1][i] = 'C'
    elif cat[1] == 1:
        for i in range(cat[0], r+1):
            dp[i][1] = 'C'
    else:
        dp[cat[0]][cat[1]] = 'C'

def path(r, c, dp):
 
    if dp[r][c] == 'C':
        return 0

    elif r == 1 or c == 1:
        dp[r][c] = 1
        return 1

    elif dp[r][c] == 0:
        dp[r][c] = path(r-1, c, dp) + path(r, c-1, dp)
        
    return dp[r][c]
 
print(path(r, c, dp))