from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()
        self.start = None

    def append(self, item):
        if self.buffer_is_full():
            temp_start = self.start
            self.start.value = item
            self.start = temp_start.next if temp_start.next is not None else self.storage.head

        elif self.storage.length == 0:
            self.storage.add_to_head(item)
            self.start = self.storage.head

        else:
            self.storage.add_to_tail(item)
            self.end = self.storage.tail

    def buffer_is_full(self):
        if self.storage.length == self.capacity:
            return True
        else:
            return False

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        if self.storage.length > 0:
            node = self.storage.head
            while node:
                if node.value is not None:
                    list_buffer_contents.append(node.value)
                node = node.next

        return list_buffer_contents



# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass




buffer = RingBuffer(5)
buffer.append('a')
buffer.append('b')
buffer.append('c')
buffer.append('d')
buffer.append('e')
buffer.append('f')
buffer.append('g')
buffer.append('h')
buffer.append('i')
buffer.append('j')
buffer.append('k')
print(buffer.get())
