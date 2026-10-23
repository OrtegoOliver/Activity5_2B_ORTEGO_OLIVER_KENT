class ArrayStack:
    def __init__(self, capacity):
        self.data = [None] * capacity
        self.top = -1

    def is_empty(self):
        return self.top == -1

    def is_full(self):
        return self.top == len(self.data) - 1

    def push(self, value):
        if self.is_full():
            raise OverflowError("Stack overflow: Stack is full!")
        self.top = self.top + 1
        self.data[self.top] = value

    def pop(self):
        if self.is_empty():
            raise IndexError("Stack underflow: Stack is empty!")
        value = self.data[self.top]
        self.data[self.top] = None
        self.top = self.top - 1
        return value

    def peek(self):
        if self.is_empty():
            raise IndexError("Cannot peek: Stack is empty!")
        return self.data[self.top]


# Test the ArrayStack
s = ArrayStack(3)

s.push(10)
s.push(20)
s.push(30)

print("Stack data:", s.data)
print("Top value:", s.peek())
print("Removed:", s.pop())
print("Is empty:", s.is_empty())
print("Is full:", s.is_full())