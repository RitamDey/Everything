class Node:
    def __init__(self, weight):
        self.weight = weight
        self.array = [None for _ in range(26)]
        self.is_end = True

    def _get_pos(self, letter):
        return ord(letter) - 97

    def insert(self, word, weight):
        head = self

        for l in word:
            if head.array[self._get_pos(l)] == None:
                head.is_end = False
                head.array[self._get_pos(l)] = Node(weight)

            head = head.array[self._get_pos(l)]

    def search(self, word):
        head = self

        for l in word:
            pos = self._get_pos(l)
            if head.is_end == True or head.array[pos] == None:
                return -1
            head = head.array[pos]

        max_weight = -1
        for i in head.array:
            if head != None and head.weight > max_weight:
                max_weight = head.weight
        return max_weight


if __name__ == '__main__':
    root = Node(None)

    n_words, n_queries = map(int, input().split())

    for _ in range(n_words):
        ins = input().split()
        root.insert(ins[0], int(ins[-1]))

    for _ in range(n_queries):
        print(root.search(input()))

