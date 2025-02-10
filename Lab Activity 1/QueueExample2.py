from collections import deque

queue = deque()

# Add elements
queue.append(10)
queue.append(20)
queue.append(30)

# Remove element
print(queue.popleft())  # Output: 10

# Check front element
print(queue[0])  # Output: 20
