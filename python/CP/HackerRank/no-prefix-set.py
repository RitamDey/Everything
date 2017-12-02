class Node:
    def __init__(self):
        self.children = []
        for i in range(26):
            self.children.append(None)
        self.is_end = False


class Trie:
    def __init__(self):
        self.root = Node()

    def has_prefix(self, data):
        curr = self.root

        for c in data:
            pos = ord(c) - ord('a')

            if curr.is_end == True:
                return True

            if curr.children[pos] is None:
                curr.children[pos] = Node()

            curr = curr.children[pos]

        curr.is_end = True
        return False



root = Trie()
for _ in range(int(input())):
    if root.has_prefix(input()):
        print("BAD SET")
        break
else:
    print("GOOD SET")

