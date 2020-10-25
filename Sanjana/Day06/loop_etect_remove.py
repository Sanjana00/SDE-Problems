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
    
    def detect_loop(self):
        slow = self.head
        fast = self.head
        while fast:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
    
    def remove_loop(self):
        slow = self.head
        fast = self.head
        while fast:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        if slow == self.head:
            temp = self.head
            while temp.next != slow:
                temp = temp.next
            temp.next = None
            return self.head.data
        fast = self.head
        while slow.next != fast.next:
            slow = slow.next
            fast = fast.next
        slow.next = None
        return fast.next.data
        
l = LinkedList()
for i in range(10):
    l.enqueue(i + 1)
    
l.display()
print(l.detect_loop())

temp = l.head
while temp.next:
    temp = temp.next
temp.next = l.head.next.next.next

print(l.detect_loop())

print('Loop at element: {}'.format(l.remove_loop()))

l.display()
