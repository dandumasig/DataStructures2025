class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)  # Add item to the end

    def dequeue(self):
        return self.items.pop(0) if self.items else "Queue is empty!"  # Remove from front

    def peek(self):
        return self.items[0] if self.items else "Queue is empty!"  # Show front item

# Example usage
queue = Queue()
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)

print(queue.dequeue())  # Output: 10 (first item added)
print(queue.peek())  # Output: 20 (new front item)
