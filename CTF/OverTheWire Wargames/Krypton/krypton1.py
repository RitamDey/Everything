from string import ascii_lowercase, ascii_uppercase


def gen_table():
    rot13 = {}
    for i in range(len(ascii_lowercase)):
        rot13[ascii_lowercase[i]] = ascii_lowercase[(i + 13) % 26]
        rot13[ascii_uppercase[i]] = ascii_uppercase[(i + 13) % 26]
    return rot13



if __name__ == '__main__':
    cipher = input()
    rot_table = gen_table()

    for i in cipher:
        print(rot_table.get(i, i), end="")
    print("")

