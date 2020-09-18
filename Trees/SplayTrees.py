class Node(object):
    """docstring for Node."""
    def __init__(self, data = None):
        super(Node, self).__init__()
        self.data = data
        self.parent = None
        self.leftChild = None
        self.rightChild = None

class SplayTree(object):
    """docstring for SplayTree."""
    def __init__(self):
        super(SplayTree, self).__init__()
        self.root = None
    
    def left_rotate(self, x):
        y = x.rightChild
        x.rightChild = y.leftChild
        if y.leftChild != None:
            y.leftChild.parent = x
        y.parent = x.parent
        if x.parent == None:
            self.root = y
        elif x == x.parent.leftChild:
            x.parent.leftChild = y
        else:
            x.parent.rightChild = y
        y.leftChild = x
        x.parent = y
    
    def right_rotate(self, x):
        y = x.leftChild
        x.leftChild = y.rightChild
        if y.rightChild != None:
            y.rightChild.parent = x
        y.parent = x.parent
        if x.parent == None:
            self.root = y
        elif x == x.parent.rightChild:
            x.parent.rightChild = y
        else:
            x.parent.leftChild = y
        y.rightChild = x
        x.parent = y
    
    def maximum(self, x):
        while x.rightChild != None:
            x = x.rightChild
        return x
    
    def splay(self, n):
        while n.parent != None:
            if n.parent == self.root:
                if n == n.parent.leftChild:
                    self.right_rotate(n.parent)
                else:
                    self.left_rotate(n.parent)
            else:
                p = n.parent
                g = p.parent
                if n.parent.leftChild == n and p.parent.leftChild == p:
                    self.right_rotate(g)
                    self.right_rotate(p)
                elif n.parent.rightChild == n and p.parent.rightChild == p:
                    self.left_rotate(g)
                    self.left_rotate(p)
                elif n.parent.rightChild == n and p.parent.leftChild == p:
                    self.left_rotate(p)
                    self.right_rotate(g)
                else:
                    self.right_rotate(p)
                    self.left_rotate(g)
    
    def search_helper(self, n, x):
        #print(n,x)
        if x == n.data:
            self.splay(n)
            print("Found {}\n".format(x))
            return
        elif x < n.data:
            return self.search_helper(n.leftChild, x)
        elif x > n.data:
            return self.search_helper(n.rightChild, x)
        else:
            print("Not found\n")
            return
        
    def search(self, key):
        self.search_helper(self.root, key)
        
    def insert(self, val):
        new_node = Node(val)
        currentnode = self.root
        y = None
        while currentnode != None:
            y = currentnode
            if new_node.data < currentnode.data:
                currentnode = currentnode.leftChild
            else:
                currentnode = currentnode.rightChild
        new_node.parent = y
        if y == None:
            self.root = new_node
        elif new_node.data < y.data:
            y.leftChild = new_node
        else:
            y.rightChild = new_node
        self.splay(new_node)
        
    def delete(self, val):
        left_tree = SplayTree()
        right_tree = SplayTree()
        left_tree.root = self.root.leftChild
        right_tree.root = self.root.rightChild
        if left_tree.root != None:
            left_tree.root.parent = None
        if right_tree.root != None:
            right_tree.root.parent = None
        if left_tree.root != None:
            node = left_tree.maximum(left_tree.root)
            left_tree.splay(node)
            left_tree.root.rightChild = right_tree.root
            self.root = left_tree.root
        else:
            self.root = right_tree.root
    
    def inorder_helper(self,n):
        if n != None:
            self.inorder_helper(n.leftChild)
            print(n.data, end = " ")
            self.inorder_helper(n.rightChild)
    
    def inorder(self):
        self.inorder_helper(self.root)
        print("\n")

if __name__ == "__main__":
    tree = SplayTree()
    tree.insert(10)
    tree.insert(20)
    tree.insert(30)
    tree.insert(100)
    tree.insert(90)
    tree.insert(40)
    tree.insert(50)
    tree.insert(60)
    tree.insert(70)
    tree.insert(80)
    tree.insert(150)
    tree.insert(110)
    tree.insert(120)
    tree.search(40)
    tree.inorder()
    tree.delete(40)
    tree.inorder()
    