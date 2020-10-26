class Node:
    def __init__(self, value = None):
        self.data = value
        self.next = None
        self.random = None
        
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
        
    def display(self):
        if not self.head:
            print("List empty")
            return
        temp = self.head
        while temp:
            print(temp.data, end = " ")
            temp = temp.next
        print()
        
    def display_rand(self):
        if not self.head:
            print("List empty")
            return
        temp = self.head
        print()
        while temp:
            print('{} -> {}'.format(temp.data, temp.random.data))
            temp = temp.next
        print()
        
    def clone(self):
        l = LinkedList()
        temp = self.head
        while temp:
            newNode = Node(temp.data)
            newNode.next = temp.next
            temp.next = newNode
            temp = newNode.next
        temp = self.head
        while temp:
            temp.next.random = temp.random.next
            temp = temp.next.next
        temp = self.head
        l.head = self.head.next
        p = l.head
        while temp.next.next and p.next.next:
            temp.next = temp.next.next
            p.next = p.next.next
            temp = temp.next
            p = p.next
        return l

l = LinkedList()
for i in range(5):
    l.enqueue(i + 1)

l.head.random = l.head.next.next
l.head.next.random = l.head
l.head.next.next.random = l.head.next.next.next.next
l.head.next.next.next.random = l.head.next.next
l.head.next.next.next.next.random = l.head.next

l.display()
l.display_rand()

l2 = l.clone()
l2.display()
l2.display_rand()
