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
    
    def reverse_k(self, k):
        temp = self.head
        p = self.head
        c = 0
        stack = []
        while temp:
            while temp and c < k:
                stack.append(temp.data)
                temp = temp.next
                c += 1
            while c > 0:
                p.data = stack.pop()
                p = p.next
                c -= 1
        
l = LinkedList()
for i in range(12):
    l.enqueue(i + 1)

l.display()

k = int(input())
l.reverse_k(k)

l.display()
