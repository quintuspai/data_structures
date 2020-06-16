class Node(object):
    """docstring for Node."""
    def __init__(self, data):
        super(Node, self).__init__()
        self.data = data
        self.leftChild = None
        self.rightChild = None
        self.rThread = 0
        self.lThread = 0
    
    def get_data(self):
        return self.data
    
    def get_leftChild(self):
        return self.leftChild
    
    def get_rightChild(self):
        return self.rightChild
    
    def get_rThread(self):
        return self.rThread
    
    def get_lThread(self):
        return self.lThread
    
    def set_leftChild(self, new_child):
        self.leftChild = new_child
    
    def set_rightChild(self, new_child):
        self.rightChild = new_child
    
    def set_lThread(self, val):
        self.lThread = val
    
    def set_rThread(self, val):
        self.rThread = val

class DoubleThreadedTree(object):
    """docstring for DoubleThreadedTree."""
    def __init__(self):
        super(DoubleThreadedTree, self).__init__()
        self.dummyNode = Node(None)
        self.dummyNode.set_lThread(0)
        self.dummyNode.set_rThread(1)
        self.dummyNode.set_leftChild(self.dummyNode)
        self.dummyNode.set_rightChild(self.dummyNode)
    
    def insert(self, data):
        new_node = Node(data)
        if self.dummyNode.get_leftChild() == self.dummyNode and self.dummyNode.get_rightChild() == self.dummyNode:
            new_node.set_leftChild(self.dummyNode)
            self.dummyNode.set_leftChild(new_node)
            new_node.set_lThread(self.dummyNode.get_lThread())
            self.dummyNode.set_lThread(1)
            new_node.set_rightChild(self.dummyNode)
        else:
            lFlag = rFlag = None
            current = self.dummyNode.get_leftChild()
            while True:
                if data < current.get_data():
                    if current.get_lThread() == 0:
                        lFlag = True
                        rFlag = False
                        break
                    else:
                        current = current.get_leftChild()
                else:
                    if current.get_rThread() == 0:
                        lFlag = False
                        rFlag = True
                        break
                    else:
                        current = current.get_rightChild()
            if lFlag:
                new_node.set_leftChild(current.get_leftChild())
                current.set_leftChild(new_node)
                new_node.set_lThread(current.get_lThread())
                current.set_lThread(1)
                new_node.set_rightChild(current)
            if rFlag:
                new_node.set_rightChild(current.get_rightChild())
                current.set_rightChild(new_node)
                new_node.set_rThread(current.get_rThread())
                current.set_rThread(1)
                new_node.set_leftChild(current)
      
    def display(self):
        current = self.dummyNode.get_leftChild()
        while current.get_lThread() == 1:
            current = current.get_leftChild()
        while current != self.dummyNode:
            print(current.get_data(), end=' ')
            current = self.findNextNode(current)
            
    def findNextNode(self, node):
        if node.get_rThread() == 0:
            return node.get_rightChild()
        node = node.get_rightChild()
        while node.get_lThread() != 0:
            node = node.get_leftChild()
        return node
      
if __name__ == '__main__':
    dtt = DoubleThreadedTree()
    dtt.insert(6)
    dtt.insert(3)
    dtt.insert(8)
    dtt.insert(1)
    dtt.insert(5)
    dtt.insert(7)
    dtt.insert(11)
    dtt.insert(9)
    dtt.insert(13)
    dtt.display()