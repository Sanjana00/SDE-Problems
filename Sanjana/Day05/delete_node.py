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
        
    def delete(self, node):
        temp = node.data
        if node == self.head:
            self.head = self.head.next
        elif node.next:
            node.data = node.next.data
            node.next = node.next.next
        else:
            p = self.head
            while p.next.next:
                p = p.next
            p.next = None
        return temp
        
l = LinkedList()
for _ in range(3):
    l.enqueue(_)

l.display()

print('\nDeleted: {}\n'.format(l.delete(l.head.next)))

l.display()
