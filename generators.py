class LinkedList:

    def __init__(self, collection=None):
        self.head = None
        self.length = 0
        if collection:
            for item in reversed(collection):
                self.insert(item)


    def __iter__(self):

        def value_generator():

            current = self.head
            while current:
                yield current.value
                current = current.next

        return value_generator()

    def __str__(self):

        output = ""

        for val in self:
            output += f"[ {val} ] -> "

        return output + "None"

    def __len__(self):

        return len(list(iter(self)))

    def insert(self, value):
        self.head = Node(value, self.head)

class Node:
    def __init__(self, value, next_ = None):
        self.value = value
        self.next = next_
