# Method only submission
#

def reverse(head):
    curr = head
    prev = None

    while curr:
        curr.prev, curr.next = curr.next, curr.prev
        prev = curr
        curr = curr.prev

    return prev
