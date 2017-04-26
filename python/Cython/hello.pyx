cdef class LinkedList:
    cdef public object data
    cdef LinkedList next_node
    cdef LinkedList prev_node

    def __cinit__(self, object data):
        self.next_node = None
        self.prev_node = None

    def __init__(self, object data):
        self.data = data

    def append(self, object data):
        list = self
        while list.next_node:
            list = list.next_node
        list.next_node = LinkedList(data)
        list.next_node.prev_node = list
        list.next_node.next_node = None

    def __str__(self):
        return "<LinkedList %s>" %self.data

    def __repr__(self):
        return "<LinkedList %s>" %self.data

    def __add__(self, object other):
        self.append(other)
        return self

    def __iadd__(self, object other):
        self.append(other)
