class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop() if self.items else "Stack is empty!"

    def peek(self):
        return self.items[-1] if self.items else "Stack is empty!"

# Example usage
stack = Stack()
stack.push(10)
stack.push(20)

print(stack.pop())  # Output: 20
print(stack.peek())  # Output: 10
