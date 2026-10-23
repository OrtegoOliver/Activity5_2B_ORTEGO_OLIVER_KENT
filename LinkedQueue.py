class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedQueue:
    def __init__(self):
        self.front = None
        self.rear = None

    def is_empty(self):
        return self.front is None

    def enqueue(self, value):
        node = Node(value)

        if self.is_empty():
            self.front = node
        else:
            self.rear.next = node

        self.rear = node

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue underflow")

        value = self.front.value
        self.front = self.front.next

        if self.front is None:
            self.rear = None

        return value

    def peek_front(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.front.value



queue = LinkedQueue()
queue.enqueue("A")
queue.enqueue("B")
queue.enqueue("C")

print("Front:", queue.peek_front())
print("Removed:", queue.dequeue())
print("New front:", queue.peek_front())