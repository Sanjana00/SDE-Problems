class Node:
    def __init__(self, value = None):
        self.data = value
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None
        
    def enqueue(self, value):
        newNode = Node(value)
        if not self.head:
            self.head = newNode
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = newNode
    
    def dequeue(self):
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
        
    def merge(self, l):
        p1 = self.head
        p2 = l.head
        new_l = LinkedList()
        while p1 and p2:
            if p1.data < p2.data:
                new_l.enqueue(p1.data)
                p1 = p1.next
            else:
                new_l.enqueue(p2.data)
                p2 = p2.next
        while p1:
            new_l.enqueue(p1.data)
            p1 = p1.next
        while p2:
            new_l.enqueue(p2.data)
            p2 = p2.next
            
        return new_l
        
l1 = LinkedList()
for _ in range(1, 15, 3):
    l1.enqueue(_)
    
l1.display()

l2 = LinkedList()
for _ in range(1, 10, 2):
    l2.enqueue(_)
    
l2.display()

l3 = l1.merge(l2)
l3.display()
