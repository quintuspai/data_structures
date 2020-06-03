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

class DoubleLinkedList(object):
    """docstring for DoubleLinkedList."""
    def __init__(self, head = None):
        super(DoubleLinkedList, self).__init__()
        self.head = head
    
    def insert_beg(self, data):
        new_node = Node(data)
        if self.head is not None:
            self.head.set_prev(new_node)
            new_node.set_next(self.head)
        self.head = new_node
    
    def insert_end(self, data):
        new_node = Node(data)
        current = self.head
        while current.get_next() != None:
            current = current.get_next()
        current.set_next(new_node)
        new_node.set_prev(current)
    
    def insert_before(self, data, val):
        current = self.head
        isFound = False
        previous = None
        while current.get_next() != None or isFound is False:
            if current.get_data() == val:
                isFound = True
            else:
                previous = current
                current = current.get_next()
        if isFound is False:
            print("{} not found for inserting\n".format(val))
        else:
            new_node = Node(data)
            if previous is None:
                new_node.set_next(self.head)
                self.head.set_prev(new_node)
                self.head = new_node
            else:
                previous.set_next(new_node)
                new_node.set_prev(previous)
                new_node.set_next(current)
                current.set_prev(new_node)
            
    def delete(self, val):
        current = self.head
        previous = None
        isFound = False
        while current.get_next() != None or isFound is False:
            if current.get_data() == val:
                isFound = True
            else:
                previous = current
                current = current.get_next()
        if isFound is False:
            print("{} not found to delete.\n".format(val))
        if previous is None:
            self.head = current.get_next()
            self.head.set_prev(None)
        elif current.get_next() == None:
            previous.set_next(None)
            current.set_prev(None)
        else:
            previous.set_next(current.get_next())
            current.get_next().set_prev(previous)
            
        
    def size(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.get_next()
        print("The size is {} \n".format(count))
    
    def search(self, val):
        current = self.head
        isFound = False
        while  current != None and isFound is False:
            if current.get_data() == val:
                isFound = True
            else:
                current = current.get_next()
        if isFound is False:
            print("{} not found \n".format(val))
        else:
            print("{} found \n".format(val))
    
    def display(self):
        current = self.head
        while current != None:
            print("{} ".format(current.get_data()))
            current = current.get_next()
        print('\n')

if __name__ == '__main__':
    dll = DoubleLinkedList()
    dll.insert_beg(1)
    dll.insert_beg(3)
    dll.insert_beg(4)
    dll.insert_beg(5)
    dll.insert_end(0)
    dll.display()
    dll.delete(0)
    dll.display()
    dll.insert_before(2,1)
    dll.display()