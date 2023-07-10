friends = [[],[6],[6],[4,5,6,15],[3,5,6],[3,4,6],[1,2,3,4,5,7],[6,8],[7,9],[8,10,12],[9,11],[10,12],[9,11,13],[12,14,15],[13],[3,13],[17,18],[16,18],[16,17],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]

def i(x, y):
    friends[x].append(y)
    friends[y].append(x)
    
    print(friends)
    return friends

while 1:
    task = input()

    if task == 'q':
        break

    if task == 'i':
        print('BURH')
        x, y = int(input()), int(input())
        friends = i(x, y)
