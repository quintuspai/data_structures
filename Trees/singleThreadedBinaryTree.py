class Node(object):
    """docstring for Node."""
    def __init__(self, data, leftChild = None, rightChild = None, rThread = False):
        super(Node, self).__init__()
        self.data = data
        self.leftChild = leftChild
        self.rightChild = rightChild
        self.rThread = rThread
    
    def get_data(self):
        return self.data
    
    def get_leftChild(self):
        return self.leftChild
    
    def get_rigthChild(self):
        return self.rightChild
    
    def get_rThread(self):
        return self.rThread
    
    def set_leftChild(self, new_child):
        self.leftChild = new_child
    
    def set_rightChild(self, new_child):
        self.rightChild = new_child
    
    def set_rThread(self, val):
        self.rThread = val

class ThreadedBinaryTree(object):
    """docstring for ThreadedBinaryTree."""
    def __init__(self):
        super(ThreadedBinaryTree, self).__init__()
        self.root = None
    
    def insert_node(self, data):
        new_node = Node(data)
        if self.root is None:
            self.root = new_node
        else:
            parentptr = None
            currentptr = self.root
            while currentptr != None:
                parentptr = currentptr
                if data < currentptr.get_data():
                    currentptr = currentptr.get_leftChild()
                    if currentptr is None:
                        parentptr.set_leftChild(new_node)
                        new_node.set_rightChild(parentptr)
                        new_node.set_rThread(True)
                        break
                else:
                    if currentptr.get_rThread() is False:
                        currentptr = currentptr.get_rigthChild()
                        if currentptr is None:
                            parentptr.set_rightChild(new_node)
                            break
                    else:
                        temp = currentptr.get_rigthChild()
                        currentptr.set_rightChild(new_node)
                        new_node.set_rightChild(temp)
                        new_node.set_rThread(True)
                        break
    
    def display(self):
        current = self.left_most(self.root)
        while current != None:
            print(current.get_data(), end=' ')
            if current.get_rThread():
                current = current.get_rigthChild()
            else:
                current = self.left_most(current.get_rigthChild())
            
    def left_most(self, node):
        if node is None:
            return None
        else:
            while node.get_leftChild() != None:
                node = node.get_leftChild()
            return node
    
if __name__ == '__main__':
    tbt = ThreadedBinaryTree()
    tbt.insert_node(5)
    tbt.insert_node(8)
    tbt.insert_node(2)
    tbt.insert_node(3)
    tbt.insert_node(7)
    tbt.display()