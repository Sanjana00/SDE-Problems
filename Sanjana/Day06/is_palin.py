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
    
    def mid_node(self):
        slow = self.head
        fast = self.head
        
        while fast:
            fast = fast.next
            if fast and fast.next:
                slow = slow.next
                fast = fast.next
                
        return slow
    
    def reverse(self, node):
        prev = None
        current = node
        temp = None
        
        while current:
            temp = current.next
            current.next = prev
            prev = current
            current = temp
            
        self.head = prev
    
    def is_palin(self):
        new_head = self.mid_node()
        l = LinkedList()
        l.head = new_head.next
        l.reverse(new_head.next)
        temp1 = self.head
        temp2 = l.head
        while temp1 and temp2:
            if temp1.data != temp2.data:
                return False
            temp1 = temp1.next
            temp2 = temp2.next
        return True
        
l1 = LinkedList()
for i in [1, 2, 3, 4, 5, 4, 3, 2, 1]:
    l1.enqueue(i)
    
l2 = LinkedList()
for i in range(10):
    l2.enqueue(i + 1)
    
l3 = LinkedList()
for i in [1, 2, 3, 3, 2, 1]:
    l3.enqueue(i)
    
l1.display()
print(l1.is_palin())

l2.display()
print(l2.is_palin())

l3.display()
print(l3.is_palin())
