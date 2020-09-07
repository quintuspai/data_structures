class Node(object):
    """docstring for Node."""
    def __init__(self, data = None, priority = None):
        super(Node, self).__init__()
        self.data = data
        self.next = None
        self.priority = priority
    
    def get_data(self):
        return self.data
    
    def get_priority(self):
        return self.priority
    
    def get_next(self):
        return self.next
    
    def set_data(self, val):
        self.data = val
        
    def set_next(self, new_next):
        self.next = new_next
        
    def set_priority(self, p):
        self.priority = p
        
class PriorityQueue(object):
    """docstring for PriorityQueue."""
    def __init__(self):
        super(PriorityQueue, self).__init__()
        self.head = None
        
    def insert(self, data, priority):
        new_node = Node(data, priority)
        if self.head is None or priority < self.head.get_priority():
            new_node.set_next(self.head)
            self.head = new_node
        else:
            currentnode = self.head
            while currentnode.get_next() != None and currentnode.get_next().get_priority() <= priority:
                currentnode = currentnode.get_next()
            new_node.set_next(currentnode.get_next())
            currentnode.set_next(new_node)

    def delete(self):
        if self.head is None:
            print("Underflow\n")
        else:
            print("Deleted item {}\n".format(self.head.get_data()))
            self.head = self.head.get_next()
    
    def display(self):
        current = self.head
        if current is None:
            print('Underflow\n')
        else:
            while current != None:
                print("{} [priority = {}]\n".format(current.get_data(), current.get_priority()))
                current = current.get_next()


if __name__ == "__main__":
    a = PriorityQueue()
    a.insert('C',3)
    a.insert("A",1)
    a.insert("B",2)
    a.insert("E",6)
    a.insert("D",5)
    a.insert("F",2)
    a.display()
    a.delete()
    a.display()