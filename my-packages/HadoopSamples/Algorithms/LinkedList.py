class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add(self, data):
        if self.head is None:
            n = Node(data)
            self.head = n
            self.tail = n
        else:
            print("adding to end")
            # we are adding new items to end of list
            n = Node(data)

            # two steps
            # 1. move object at the end to point to new item
            self.tail.next = n

            # 2. move the tail pointer to the new item
            self.tail = n

    def display(self):
        if self.head is None:
            print("List is empty")
        else:
            current = self.head
            while current is not None:
                print(current.data)
                current = current.next
            print("End of list")


l = LinkedList()
l.add(1)
l.add(2)
l.add(3)
l.add(4)
l.display()
