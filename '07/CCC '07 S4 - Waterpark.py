import sys
n = int(input())

graph = [[] for x in range(n+1)]
dp = [0 for x in range(n+1)]
dp[1] = 1

while True:
    a, b = [int(x) for x in input().split()]
    if a == 0 and b == 0:
        break
    graph[a].append(b)

for i in range(1, n+1):
    for j in graph[i]:
        dp[j] += dp[i]

print(dp[n])