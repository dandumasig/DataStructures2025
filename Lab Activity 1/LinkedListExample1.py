class Node:
    def __init__(self, data):
        self.data = data  # Store data
        self.next = None  # Pointer to next node

class LinkedList:
    def __init__(self):
        self.head = None  # Start of the list

    def append(self, data):
        """Add a node at the end"""
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def display(self):
        """Print the linked list"""
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

# Example usage
ll = LinkedList()
ll.append(10)
ll.append(20)
ll.append(30)
ll.display()  # Output: 10 -> 20 -> 30 -> None
