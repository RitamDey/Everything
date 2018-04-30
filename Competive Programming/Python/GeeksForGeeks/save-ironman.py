def santize(string):
    res = ""

    for i in string:
        if i.isalnum():
            res += i

    return i


for _ in range(int(input())):
    string = input().lower()
    string = sanitize(string)

    print("YES" if string == string[::-1] else "NO")

