brackets = input()
bracket_set = {"{":"}", "[":"]","(":")"}
opening_braces = []
closing_braces = []

for brace in brackets:
    if brace in bracket_set.keys():
        opening_braces.append(brace)
    else:
        closing_braces.append(brace)

print(opening_braces, closing_braces[::-1], opening_braces == closing_braces[::-1])
