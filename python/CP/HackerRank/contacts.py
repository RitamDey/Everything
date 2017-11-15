class Trie:
    class Node:
        def __init__(self):
            self.is_end = False
            self.children = [None,]*26
            self.count = 0

    def __init__(self):
        self.root = self.Node()

    def insert(self, word):
        curr = self.root

        for c in word:
            pos = ord(c) - ord('a')

            if curr.children[pos] is None:
                curr.children[pos] = self.Node()
            curr.count += 1

            curr = curr.children[pos]

        curr.is_end = True

    def find(self, word):
        curr = self.root

        for c in word:
            pos = ord(c) - ord('a')

            if curr.children[pos] is None:
                return 0

            curr = curr.children[pos]

        if curr is not None:
            return curr.count


if __name__ == '__main__':
    root = Trie()

    for _ in range(int(input())):
        t, arg = input().split()

        if t == 'add':
            root.insert(arg)
        else:
            print(root.find(arg))
