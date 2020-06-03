#Grounded_header_linked_list
class Node(object):
    """docstring for Node."""
    def __init__(self, data, next = None):
        super(Node, self).__init__()
        self.data = data
        self.next = next
    
    def get_data(self):
        return self.data
    
    def update_data(self, new_data):
        self.data = new_data
    
    def get_next(self):
        return self.next
    
    def set_next(self, new_next):
        self.next = new_next

class HeaderLinkedList(object):
    """docstring for HeaderLinkedList."""
    def __init__(self, head = None):
        super(HeaderLinkedList, self).__init__()
        #|size|start_node|last_node| => header node structure
        header_list = ['0', head, head]
        self.head = Node(header_list)
    
    def insert(self, data):
        new_node = Node(data)
        if self.head.get_next() == None:
            header_node = self.head.get_data()
            header_node[0] = 1
            header_node[1] = header_node[2] = new_node
            self.head.update_data(header_node)
            self.head.set_next( new_node)
        else:
            header_node = self.head.get_data()
            header_node[0] = header_node[0] + 1
            header_node[1] = new_node
            self.head.update_data(header_node)
            new_node.set_next(self.head.get_next())
            self.head.set_next(new_node)
            
    def display(self):
        header_node = self.head.get_data()
        current = header_node[1]
        while current != None:
            print(current.get_data())
            current = current.get_next()
        print("\n")
        
    def size_ll(self):
        header_node = self.head.get_data()
        print("The size of the list is {}".format(header_node[0]))
        
    def search(self, val):
        current = self.head.get_next()
        isFound = False
        while current != None and isFound is False:
            if current.get_data() == val:
                isFound = True
            else:
                current = current.get_next()
        if isFound is False:
            print('{} not found\n'.format(val))
        else:
            print('{} found \n'.format(val))
        
    def delete_beg(self):
        header_node = self.head.get_data()
        if self.head.get_next() == None:
            print("Underflow\n")
        else:
            if header_node[0] == '0':
                header_node[0] = '0'
                header_node[1] = header_node[2] = None
            else:
                header_node[0] = header_node[0] - 1
                header_node[1] = self.head.get_next().get_next()
            self.head.update_data(header_node)
            
            
if __name__ == '__main__':
    a = HeaderLinkedList()
    a.insert(1)
    a.insert(2)
    a.insert(3)
    a.insert(4)
    a.insert(5)
    a.display()
    a.delete_beg()
    a.display()