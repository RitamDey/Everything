pad = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
      ]


def move(instruction, pos):
    """
    The 0 represents Row in the Array
    The 1 represents Column in the Array
    """
    for i in instruction:
        if i == 'U':
            pos['row'] -= 1
            if pos['row'] < 0:
                pos['row'] = 0
        elif i == 'D':
            pos['row'] += 1
            if pos['row'] > 2:
                pos['row'] = 2
        elif i == 'L':
            pos['col'] -= 1
            if pos['col'] < 0:
                pos['col'] = 0
        else:
            pos['col'] += 1
            if pos['col'] > 2:
                pos['col'] = 2
    return pos, pad[pos['row']][pos['col']]


if __name__ == '__main__':
    instructions = open('input.txt').read().split('\n')[0:-1]
    pos = {'row': 1, 'col': 1}
    for i in instructions:
        pos, r = move(i, pos)
        print(pos)
        print(r)

