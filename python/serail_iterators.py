class LinkedList:
    def __init__(self, data, next_node=None):
        self._data = data
        self._next = next_node

    def append(self, data):
        if self._next:
            self._next.append(data)
        else:
            self._next = LinkedList(data)

    def __iter__(self):
        return serial_iter(self)


def serial_iter(object):
    while object:
        yield object._data
        object = object._next
    raise StopIteration

