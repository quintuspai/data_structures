class Node(object):
    """docstring for Node."""
    def __init__(self, data, prev = None, next = None):
        super(Node, self).__init__()
        self.prev = prev
        self.data = data
        self.next = next
    
    def get_data(self):
        return self.data
    
    def get_prev(self):
        return self.prev
    
    def get_next(self):
        return self.next
    
    def set_prev(self, new_prev):
        self.prev = new_prev
        
    def set_next(self, new_next):
        self.next = new_next

class CircularDoubleLinkedList(object):
    """docstring for CircularDoubleLinkedList."""
    def __init__(self, head = None):
        super(CircularDoubleLinkedList, self).__init__()
        self.head = head
    
    def insert_beg(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            new_node.set_next(self.head)
            new_node.set_prev(self.head)
        else:
            new_node.set_prev(self.head.get_prev())
            self.head.get_prev().set_next(new_node)
            self.head.set_prev(new_node)
            new_node.set_next(self.head)
            self.head = new_node
    
    def insert_end(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            new_node.set_prev(self.head)
            new_node.set_next(self.head)
        else:
            self.head.get_prev().set_next(new_node)
            new_node.set_prev(self.head.get_prev())
            new_node.set_next(self.head)
            self.head.set_prev(new_node)
            
    def delete_beg(self):
        if self.head.get_next() == self.head:
            self.head = None
        else:
            self.head.get_prev().set_next(self.head.get_next())
            self.head.get_next().set_prev(self.head.get_prev())
            self.head = self.head.get_next()
    
    def delete_end(self):
        if self.head.get_next() == self.head:
            self.head = None
        else:
            self.head.get_prev().get_prev().set_next(self.head)
            self.head.set_prev(self.head.get_prev().get_prev())
    
    def size(self):
        current = self.head
        count = 0
        while current.get_next() != self.head:
            count = count + 1
            current = current.get_next()
        print("The size of the list is {}\n".format(count + 1))
    
    
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
    
    def display(self):
        current = self.head
        while current.get_next() != self.head:
            print(current.get_data())
            current = current.get_next()
        print(current.get_data())
        print("\n")

if __name__ == '__main__':
    ll = CircularDoubleLinkedList()
    ll.insert_beg(1)
    ll.insert_beg(2)
    ll.insert_beg(3)
    ll.insert_beg(4)
    ll.insert_beg(5)
    ll.insert_end(0)
    ll.display()
    ll.delete_end()
    ll.display()