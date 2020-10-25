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
            return
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
        
    def get_len(self):
        temp = self.head
        c = 0
        while temp:
            temp = temp.next
            c += 1
        return c
    
    def rotate(self, k):
        temp = self.head
        prev = None
        if k == 0:
            return
        while k > 0:
            k -= 1
            prev = temp
            temp = temp.next
        prev.next = None
        new_head = temp
        while temp.next:
            temp = temp.next
        temp.next = self.head
        self.head = new_head
        
l = LinkedList()
for i in range(15):
    l.enqueue(i + 1)
    
l.display()
    
n = l.get_len()
k = int(input()) % n

l.rotate(k)
l.display()
