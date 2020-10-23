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
        
    def remove_nth_back(self, n):
        back = self.head
        front = self.head
        for _ in range(n):
            front = front.next
        while front.next:
            front = front.next
            back = back.next
        temp = back.next
        back.next = back.next.next
        return temp.data
        
l = LinkedList()
for _ in range(10):
    l.enqueue(_)

l.display()

print('\nRemoved: {}\n'.format(l.remove_nth_back(7)))

l.display()
