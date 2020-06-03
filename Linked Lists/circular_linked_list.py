class Node(object):
    """docstring for Node."""
    def __init__(self, data, next = None):
        super(Node, self).__init__()
        self.data = data
        self.next = next
    
    def get_data(self):
        return self.data
    
    def get_next(self):
        return self.next
    
    def set_next(self, new_next):
        self.next = new_next
        
class CircularLinkedList(object):
    """docstring for CircularLinkedList."""
    def __init__(self, head = None):
        super(CircularLinkedList, self).__init__()
        self.head = head
    
    def insert_beg(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            new_node.set_next(self.head)
        else:
            current = self.head
            while current.get_next() != self.head:
                current = current.get_next()
            new_node.set_next(self.head)
            current.set_next(new_node)
            self.head = new_node
    
    def insert_end(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            new_node.set_next(self.head)
        else:
            current = self.head
            while current.get_next() != self.head:
                current = current.get_next()
            current.set_next(new_node)
            new_node.set_next(self.head)
            
    def delete_beg(self):
        if self.head.get_next() == self.head:
            self.head = None
        else:
            current = self.head
            while current.get_next() != self.head:
                current = current.get_next()
            current.set_next(self.head.get_next())
            self.head = self.head.get_next()
    
    def delete_end(self):
        if self.head.get_next() == self.head:
            self.head = None
        else:
            current = self.head
            previous = None
            while current.get_next() != self.head:
                previous = current
                current = current.get_next()
            previous.set_next(self.head)
    
    def search(self, val):
        current = self.head
        isFound = False 
        while current.get_next() != self.head and isFound is False:
            if current.get_data() == val:
                isFound = True
            else:
                current = current.get_next()
        if current.get_data() == val:
            isFound = True
        if isFound is False:
            print("{} not found\n".format(val))
        else:
            print("{} found\n".format(val)) 
    
    def size(self):
        current = self.head
        count = 0
        while current.get_next() != self.head:
            count = count + 1
            current = current.get_next()
        print("{} is the size\n".format(count + 1))
    
    
    def display(self):
        current = self.head
        while current.get_next() != self.head:
            print(current.get_data())
            current = current.get_next()
        print(current.get_data())
        print('\n')
        
if __name__ == '__main__':
    cll = CircularLinkedList()
    cll.insert_beg(1)
    cll.insert_beg(2)
    cll.insert_beg(3)
    cll.insert_beg(4)
    cll.insert_beg(5)
    cll.size()