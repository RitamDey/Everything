def pos(c):
    return weights[ord(c)-ord('a')]

weights = list(map(int, input().split()))
word = input()
word_max = max(map(pos, word))


print(len(word)*word_max)
