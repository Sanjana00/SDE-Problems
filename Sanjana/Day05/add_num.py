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
        
    def add_num(self, l):
        l3 = LinkedList()
        p1 = self.head
        p2 = l.head
        carry = 0
        while p1 and p2:
            s = p1.data + p2.data + carry
            carry = s // 10
            s %= 10
            l3.enqueue(s)
            p1 = p1.next
            p2 = p2.next
        while p1:
            s = p1.data + carry
            carry = s // 10
            s %= 10
            l3.enqueue(s)
            p1 = p1.next
        while p2:
            s = p2.data + carry
            carry = s // 10
            s %= 10
            l3.enqueue(s)
            p2 = p2.next
        if carry != 0:
            l3.enqueue(carry)
        return l3
        
l1 = LinkedList()
for _ in [9, 9]:
    l1.enqueue(_)

l1.rev_display()

l2 = LinkedList()
for _ in [1, 2, 3]:
    l2.enqueue(_)

l2.rev_display()

l3 = l1.add_num(l2)
l3.rev_display()
