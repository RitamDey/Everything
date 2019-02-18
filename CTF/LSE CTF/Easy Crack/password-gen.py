# A utility script to generate the solution for this challenge


def main():
    target = "\x67\x39\x66\x2E\x46\x03\x51\x76"
    eax = 0
    result = ""

    for char in target:
        result += chr(ord(char) ^ eax)
        eax += 10

    return result


if __name__ == '__main__':
    print(main())

