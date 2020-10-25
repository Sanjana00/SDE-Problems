class NNode:
    def __init__(self, value = None):
        self.data = value
        self.right = None
        self.down = None
        
class NLinkedList:
    def __init__(self):
        self.head = None
    
    def enqueue_down(self, head, value):
        temp = head
        newNode = NNode(value)
        while temp.down:
            temp = temp.down
        temp.down = newNode
        
    def enqueue(self, value):
        newNode = NNode(value)
        if not self.head:
            self.head = newNode
            return
        temp = self.head
        while temp.right:
            temp = temp.right
        temp.right = newNode
        
    def merge(self, p1, p2):
        p1.right = p1.right.right
        temp = p1
        while p1 and p2:
            if p1.data < p2.data:
                if p1.down:
                    temp = p1.down
                p1 = p1.down
                continue
            temp1 = p1.down
            p1.down = p2
            temp2 = p2
            p2 = p2.down
            temp2.down = temp1
            p1.data, temp2.data = temp2.data, p1.data
            if p1.down:
                temp = p1.down
            p1 = p1.down
        if p2:
            temp.down = p2
        
    def flatten(self):
        while self.head.right:
            self.merge(self.head, self.head.right)
            
    def display(self):
        temp1 = self.head
        while temp1:
            temp2 = temp1
            while temp2:
                print(temp2.data, end = " ")
                temp2 = temp2.down
            print()
            temp1 = temp1.right
        
l = NLinkedList()

for i in [5, 10, 19, 28]:
    l.enqueue(i)

for i in [7, 8, 30]:
    l.enqueue_down(l.head, i)
    
l.enqueue_down(l.head.right, 20)
    
for i in [22, 50]:
    l.enqueue_down(l.head.right.right, i)
    
for i in [35, 40, 45]:
    l.enqueue_down(l.head.right.right.right, i)
    
print('Before flattening:\n')
l.display()

l.flatten()

print('\nAfter flattening:\n')
l.display()
