class SerialIterator:
    def __init__(self, obj):
        self._object = obj

    def __next__(self):
        while self._object:
            yield self.object.data
            self._object = self._object._next
        raise StopIteration


class LinkedList:
    def __init__(self, data, next_node=None):
        self._data = data
        self._next = next_node

    @property
    def data(self):
        return self._data
        
    def append(self, data):
        if self._next:
            self._next.append(data)
        else:
            self._next = LinkedList(data)
        
    def __iter__(self):
        return SerialIterator(self)