from re import findall


split_re = r"\w\d+"
string = input()
final_string = ""


for word in findall(split_re, string):
    w = word[0]
    count = int(word[1:])
    final_string += word*count


print(final_string)

