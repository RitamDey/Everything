from itertools import groupby


string = input().strip()

string_count = [(len(list(count)), item) for item, count in groupby(string)]

print(*string_count)
