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
        
    def mid_node(self):
        slow = self.head
        fast = self.head
        
        while fast:
            fast = fast.next
            if fast and fast.next:
                slow = slow.next
                fast = fast.next
                
        return slow.data
        
l = LinkedList()
for _ in range(6):
    l.enqueue(_)
    
l.display()

print(l.mid_node())
