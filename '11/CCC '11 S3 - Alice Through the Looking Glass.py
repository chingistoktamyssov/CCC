def crystal(m, pos1, pos2):
    print(pos1, pos2, m)
    if m == 1:
        if pos2 == y and pos1 + 1 <= x < pos1 + 4:
            return 'crystal'
        if pos2 + 1 == y and pos1 + 2 == x:
            return 'crystal'
    
    else:

        if pos2 <= y < 5 ** (m-1) and pos1 + 5 ** (m-1) <= x < 4 * (5 ** (m-1)):
            return 'crystal'

        if pos2 + 5 ** (m-1) <= y < pos2 + 2 * (5 ** (m-1)) and pos1 + 2 * (5 ** (m-1)) <= x < pos1 + 3 * (5 ** (m-1)):
            return 'crystal'
        
        for i in [[pos1 + 5 ** (m-1), pos2 + 5 ** (m-1)], [pos1 + 3 * (5 ** (m-1)), pos2 + 5 ** (m-1)], [pos1 + 2 * (5 ** (m-1)), 2 * (pos2 + 5 ** (m-1))]]:
            if crystal(m-1, i[0], i[1]) == 'crystal':
                return 'crystal'
    
for i in range(int(input())):
    m, x, y = [int(x) for x in input().split()]

    if crystal(m, 0, 0) == 'crystal':
        print('crystal')
    else:
        print('empty')