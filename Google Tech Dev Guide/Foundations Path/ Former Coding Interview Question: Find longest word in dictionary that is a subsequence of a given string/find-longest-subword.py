def is_subword(d_word, s_word):
    subword_len = 0
    d_word_len = len(d_word)

    s_word = iter(s_word)
    d_word = iter(d_word)

    for w in d_word:
        for t in s_word:
            if w == t:
                subword_len += 1
                break

    return d_word_len == subword_len


def main():
    s = input()
    d_words = []
    while True:
        try:
            d_words.append(input())
        except EOFError:
            break
    subwords = {}

    for d in d_words:
        if is_subword(d, s):
            subwords[len(d)] = d

    print(subwords[max(subwords)])


if __name__ == '__main__':
    main()
