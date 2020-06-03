#make a linked list with all functions

class Node(object):
    """docstring for Node."""
    def __init__(self, data = None, next = None):
        super(Node, self).__init__()
        self.data = data
        self.next = next
    
    def get_data(self):
        return self.data
    
    def get_next(self):
        return self.next
    
    def set_next(self, new_node):
        self.next = new_node
    
class LinkedList(object):
    """docstring for LinkedList."""
    def __init__(self, head = None):
        super(LinkedList, self).__init__()
        self.head = None
    
    def insert_at_beg(self, data):
        new_node = Node(data)
        new_node.set_next(self.head)
        self.head = new_node
    
    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.get_next() != None:
                current = current.get_next()
            current.set_next(new_node)
    
    #insert_before,insert_after
    
    def insert_before(self, data, val):
        current = self.head
        previous = None
        isFound = False
        while current != None and isFound is False:
            if current.get_data() == val:
                isFound = True
            else:
                previous = current
                current = current.get_next()
        if isFound is False:
            print("{} data not found to insert before \n".format(val))
        if previous is None:
            self.insert_at_beg(data)
        else:
            new_node = Node(data)
            previous.set_next(new_node)
            new_node.set_next(current)
    
    def insert_after(self, data, val):
        current = self.head
        isFound = False
        while current != None and isFound is False:
            if current.get_data() == val:
                isFound = True
            else:
                current = current.get_next()
        if isFound is False:
            print("{} not found in the list \n".format(val))
        else:
            new_node = Node(data)
            new_node.set_next(current.get_next())
            current.set_next(new_node)
    
    
    def search(self, val):
        current = self.head
        isFound = False
        while current != None and isFound is False:
            if current.get_data() == val:
                isFound = True
            else:
                current = current.get_next()
        if isFound is False:
            print('Item not found \n')
        else:
            print("{} found \n".format(val))
    
    def size(self):
        current = self.head
        count = 0
        while current != None:
            count += 1
            current = current.get_next()
        print("The size of the LL is {} \n".format(count))

    def delete(self, val):
        current = self.head
        previous = None
        isFound = False
        while current != None and isFound is False:
            if current.get_data() == val:
                isFound = True
            else:
                previous = current
                current = current.get_next()
        if isFound is False:
            print("{} not found to be deleted \n".format(val))
        if previous == None:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())
    
    def display(self):
        current = self.head
        while current != None:
            print(current.get_data(),end = ' ')
            current = current.get_next()
        print('\n')
if __name__ == '__main__':
    LL = LinkedList()
    LL.insert_at_beg(1)
    LL.insert_at_beg(2)
    LL.insert_at_beg(3)
    LL.insert_at_beg(4)
    LL.display()
    LL.insert_at_end(0)
    LL.display() #proper
    LL.delete(3)
    LL.delete(1)
    LL.display()
    LL.insert_before(3,2)
    LL.display()
    LL.insert_after(1,2)
    LL.display()