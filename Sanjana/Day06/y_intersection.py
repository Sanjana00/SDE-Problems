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
    
    def rev_display(self):
        if not self.head:
            print("List empty")
            return
        temp = self.head
        l = []
        while temp:
            l.append(temp.data)
            temp = temp.next
        print(*(l[::-1]))
        
    def get_len(self):
        c = 0
        temp = self.head
        while temp:
            c += 1
            temp = temp.next
        return c
    
    def y_intersection(self, l):
        n1 = self.get_len()
        n2 = l.get_len()
        if n1 > n2:
            big = self.head
            small = l.head
        else:
            big = l.head
            small = self.head
        diff = abs(n1 - n2)
        while diff > 0:
            diff -= 1
            big = big.next
        while big != small:
            big = big.next
            small = small.next
        return big.data
        
l1 = LinkedList()
for i in range(7):
    l1.enqueue(i + 1)
l2 = LinkedList()
for i in range(7, 10):
    l2.enqueue(i)
l2.head.next.next.next = l1.head.next.next.next.next.next

l1.display()
l2.display()

print(l1.y_intersection(l2))
