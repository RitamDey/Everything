from sys import argv
import json
import string
from collections import Counter
from nltk.tokenize import TweetTokenizer
from nltk.corpus import stopwords


def process(text, tokenizer=TweetTokenizer(), stopwords=[]):
    """
    Process the text of a tweet:
        - Lowercase
        - Tokenize
        - Stopword removal
        - Digits removal
    Return: list of strings
    """
    text = text.lower()
    tokens = tokenizer.tokenize(text)
    return [tok for tok in tokens if tok not in stopwords and not tok.isdigit()]


if __name__ == "__main__":
    uname = argv[1]
    punct = list(string.punctuation)
    stopword_list = stopwords.words('english') + punct + ['rt', 'via', '...']
    tf = Counter()

    with open(uname, 'r') as fout:
        for line in fout.readlines():
            tokens = process(text=line, stopwords=stopword_list)
            tf.update(tokens)

    for tag, count in tf.most_common(20):
        print("{}: {}".format(tag, count))
