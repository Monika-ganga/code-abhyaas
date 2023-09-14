class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def addNodeAtLast(self, data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = newNode

    def traverse(self):
        current = self.head
        while current:
            print(current.data, end=' --> ')
            current = current.next
        print('Null')

    def findMiddle(self):
        if self.head is None:
            return None

        slow = self.head
        fast = self.head

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

        return slow.data

# Create an instance of the LinkedList class
myLinkedList = LinkedList()

# Add nodes to the linked list
myLinkedList.addNodeAtLast(10)
myLinkedList.addNodeAtLast(20)
myLinkedList.addNodeAtLast(30)
myLinkedList.addNodeAtLast(40)
myLinkedList.addNodeAtLast(50)

# Traverse and print the linked list
myLinkedList.traverse()

# Find the middle element
middle_element = myLinkedList.findMiddle()
print("Middle element:", middle_element)
