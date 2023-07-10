friends = [[],[6],[6],[4,5,6,15],[3,5,6],[3,4,6],[1,2,3,4,5,7],[6,8],[7,9],[8,10,12],[9,11],[10,12],[9,11,13],[12,14,15],[13],[3,13],[17,18],[16,18],[16,17],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]

def i(x, y):
    if y not in friends[x]:
        friends[x].append(y)
    if x not in friends[y]:
        friends[y].append(x)
    
    return friends

def d(x, y):
    friends[x].remove(y)
    friends[y].remove(x)

    return friends

def f(x):
    first = friends[x]
    counted = []

    for i in first:
        for j in friends[i]:
            if j not in counted and j not in first and j != x:
                counted.append(j)
    
    print(len(counted))

def s(x, y):
    shortest = [float('inf')] * len(friends)
    shortest[x] = 0

    queue = [x]
    visited = []

    while queue:
        node = queue.pop(0)
        visited.append(node)

        if node == y:
            break

        for i in friends[node]:
            if i not in queue and i not in visited:
                queue.append(i)
                shortest[i] = min(shortest[node]+1, shortest[i])

    if shortest[y] == float('inf'):
        print('Not connected')
    else:
        print(shortest[y])

while 1:
    task = input()

    if task == 'q':
        break

    if task == 'i':
        x, y = int(input()), int(input())
        friends = i(x, y)

    if task == 'd':
        x, y = int(input()), int(input())
        friends = d(x, y)

    if task == 'n':
        x = int(input())
        print(len(friends[x]))

    if task == 'f':
        x = int(input())
        f(x)
    
    if task == 's':
        x, y = int(input()), int(input())
        s(x, y)