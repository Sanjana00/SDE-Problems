class Node:
    def __init__(self, value = None):
        self.data = value
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None
        
    def enQueue(self, value):
        newNode = Node(value)
        if not self.head:
            self.head = newNode
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = newNode
    
    def deQueue(self):
        if not self.head:
            return False
        temp = self.head
        self.head = self.head.next
        return temp.data
    
    def display(self):
        if not self.head:
            print("List empty")
            return
        temp = self.head
        while temp:
            print(temp.data, end = " ")
            temp = temp.next
        print()
        
    def reverse(self):
        prev = None
        current = self.head
        temp = None
        
        while current:
            temp = current.next
            current.next = prev
            prev = current
            current = temp
            
        self.head = prev
        
l = LinkedList()
for _ in range(6):
    l.enQueue(_)
    
l.display()

l.reverse()
l.display()
