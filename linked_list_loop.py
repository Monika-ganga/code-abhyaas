class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def addNodeAtLast(self, data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode

    def traverse(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next
    def isCircular(self):
        if(self.head==None):
            return False
        slow=self.head
        fast=self.head.next
        while(fast!=None and fast.next!=None):
            if( slow == fast):
                return True
            slow=slow.next
            fast=fast.next.next
        return False
                
	        

# Create an instance of the LinkedList class
obj = LinkedList()

# Add nodes to the linked list
obj.addNodeAtLast(10)
obj.addNodeAtLast(20)
obj.addNodeAtLast(30)
obj.addNodeAtLast(40)

# Traverse and print the linked list
obj.traverse()
result=obj.isCircular()
print(result)
