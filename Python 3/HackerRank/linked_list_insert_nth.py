class Node:
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next = next_node


def insertNth(linked_list, data, position):
    head = linked_list
    if position==0:
        tmp = Node(data, head)
        return tmp
    else:
        while head.next.next:
            head = head.next
        tmp = Node(data, head.next.next)
        head.next = tmp
    print("Head's data ", head.data,"Head's next node's data ", head.next.data)
    return linked_list


if __name__ == '__main__':
    linked_list = Node()
    for _ in range(int(input("Enter number of tests: "))):
        pos, data = list(map(int, input("Enter position and data: ").split()))
        
        linked_list = insertNth(linked_list, data, pos)
    
    while linked_list:
        print(linked_list.data)
        linked_list = linked_list.next
