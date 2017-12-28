class Node:
    def __init__(self, data, next_node=None, prev_node=None):
        self.data = data
        self.next = next_node
        self.prev = prev_node

    def __str__(self):
        print(self.data)
        if self.next:
            self.next.__str__()


def SortedInsert(head, data):
    if head is None:
        return Node(data)

    if data < head.data
        node = Node(data, head)
        head.prev = node
        return node

    tmp = head.next
    while tmp.next:
        if data < tmp.data:
            break
        tmp = tmp.next

    node = Node(data, tmp, tmp.prev)
    tmp.prev.next = node
    tmp.prev = node

    return head

