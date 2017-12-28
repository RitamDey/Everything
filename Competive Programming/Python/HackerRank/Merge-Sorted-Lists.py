class Node:
    data = None
    next = None
    def __init__(self, data, next_node=None):
        self.data = data
        self.next = next_node

    def __repr__(self):
        return self.data


def append(node_list, data):
    if node_list.next:
        append(node_list.next, data)
    else:
        node_list.next = Node(data)


def merge(list1, list2):
    merged = Node('tmp')
    tmp = merged

    while list1 is not None and list2 is not None:
        if list1.data < list2.data:
            add = list1
            list1 = list1.next
        else:
            add = list2
            list2 = list2.next

        tmp.next = add
        tmp = tmp.next

        # print("Added %d" % add.data)

    while list1 is not None:
        tmp.next = list1
        list1 = list1.next
        tmp = tmp.next

    while list2 is not None:
        tmp.next = list2
        list2 = list2.next
        tmp = tmp.next

    return merged.next


if __name__ == '__main__':
    l1 = Node(1)
    append(l1, 3)
    append(l1, 5)
    append(l1, 6)

    l2 = Node(2)
    append(l2, 4)
    append(l2, 7)

    l3 = merge(l1, l2)

    while l3:
        print(l3.data)
        l3 = l3.next

