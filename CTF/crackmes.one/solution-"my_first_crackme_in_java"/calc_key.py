from string import ascii_lowercase, ascii_uppercase


def calc_key(name, n1=ord('a'), n2=ord('n'), n3=ord('d')):
    name_sum = 0
    for i in name:
        if i in ascii_lowercase+ascii_uppercase:
            name_sum += ord(i)

    name_sum <<= 2
    c2 = name_sum & 255
    c3 = c2 ^ name_sum
    c4 = c3 | name_sum

    d = (((((c2 * 2) + (c3 * 3)) + (c4 * 4)) + (n1 * 10)) + (n2 * 11)) + (n3 * 12)

    print(f"name_sum = {name_sum}\nc2       = {c2}\nc3       = {c3}")
    print(f"c4       = {c4}\nd        = {d}")


if __name__ == '__main__':
    calc_key("Ritam")

