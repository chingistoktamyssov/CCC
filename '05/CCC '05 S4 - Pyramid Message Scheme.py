l = int(input())

def bfs(node):
    queue = [node]
    visited = [node]
    count = 0

    while queue:
        for i in range(len(queue)):
            explore = queue.pop(0)
            for j in graph[explore]:
                if j not in visited:
                    queue.append(j)
                    visited.append(j)
        count += 10
    return count - 10

for i in range(l):

    n = int(input())

    peopleScheme = []
    for j in range(n):
        name = input()
        peopleScheme.append(name)
    
    graph = {}
    for j in range(n):
        if j == n-1:
            if peopleScheme[j] not in graph:
                graph[peopleScheme[j]] = [peopleScheme[0]]
            else:
                graph[peopleScheme[j]].append(peopleScheme[0])
        else:
            if peopleScheme[j] not in graph:
                graph[peopleScheme[j]] = [peopleScheme[j+1]]
            else:
                graph[peopleScheme[j]].append(peopleScheme[j+1])

    speed = bfs(peopleScheme[-1]) * 2
    print(len(peopleScheme) * 10 - speed)