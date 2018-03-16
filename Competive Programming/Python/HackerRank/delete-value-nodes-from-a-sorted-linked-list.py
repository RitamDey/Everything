"""
This was a method only submission. Thus only the method is written here.
The structure of Node class was

class Node:
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next = next_node

The method returns the head node, which could also be supplied as None
"""
def RemoveDuplicates(head: Node):
    if head is None:
        return head

    tmp = head

    while tmp and tmp.next:
        if tmp.data == tmp.next.data:
            tmp.next =  tmp.next.data
        else:
            # don't just increment the pointer in list.
            # This node could also be a duplicate of the previous one
            tmp = tmp.next

    return head

