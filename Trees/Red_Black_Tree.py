import sys
class Node(object):
    """docstring for Node."""
    def __init__(self, data = None, parent = None):
        super(Node, self).__init__()
        self.data = data
        self.parent = parent
        self.leftChild = None
        self.rightChild = None
        self.color = 1 #1->Red
        
class RedBlackTree(object):
    """docstring for RedBlackTree."""
    def __init__(self):
        super(RedBlackTree, self).__init__()
        self.NULL = Node()
        self.NULL.color = 0
        self.root = self.NULL
    
    def perfrom_preorder(self, root):
        if root != None:
            print(root.data, end = ' ')
            self.perfrom_preorder(root.leftChild)
            self.perfrom_preorder(root.rightChild)
        
    def preorder_traversal(self):
        self.perfrom_preorder(self.root)
        print('\n')
        
    def perfrom_inorder(self, root):
        if root != None:
            self.perfrom_inorder(root.leftChild)
            print(root.data, end= ' ')
            self.perfrom_inorder(root.rightChild)
        
    def inorder_traversal(self):
        self.perfrom_inorder(self.root)
        print("\n")
        
    def perfrom_postorder(self, root):
        if root != None:
            self.perfrom_postorder(root.leftChild)
            self.perfrom_postorder(root.rightChild)
            print(root.data, end = ' ')
    
    def postorder_traversal(self):
        self.perform_postorder(self.root)
        print("\n")
    
    def left_rotate(self, x):
        y = x.rightChild
        x.rightChild = y.leftChild
        if y.leftChild != self.NULL:
            y.leftChild.parent = x
        y.parent = x.parent
        if x.parent == None:
            self.root = y
        elif x == x.parent.leftChild:
            x.parent.left = y
        else:
            x.parent.rightChild = y
        y.leftChild = x
        x.parent = y
        
    def right_rotate(self, x):
        y = x.leftChild
        x.leftChild = y.rightChild
        if y.rightChild != self.NULL:
            y.rightChild.parent = x
        y.parent = x.parent
        if x.parent == None:
            self.root = y
        elif x == x.parent.rightChild:
            x.parent.rightChild = y
        else:
            x.parent.leftChild = y
        y.righChild = x
        x.parent = y
    
    def fix_insert(self, z):
        while z.parent.color == 1:
            if z.parent == z.parent.parent.leftChild:
                y = z.parent.parent.rightChild
                if y.color == 1:
                    z.parent.color = 0
                    y.color = 0
                    z.parent.parent.color = 1
                    z = z.parent.parent
                else:
                    if z == z.parent.rightChild:
                        z = z.parent
                        self.left_rotate(z)
                    z.parent.color = 0
                    z.parent.parent.color = 1
                    self.right_rotate(z.parent.parent)
            else:
                y = z.parent.parent.rightChild
                if y.color == 1:
                    z.parent.color = 0
                    y.color = 0
                    z.parent.parent.color = 1
                    z = z.parent.parent
                else:
                    if z == z.parent.leftChild:
                        z = z.parent
                        self.right_rotate(z)
                    z.parent.color = 0
                    z.parent.parent.color = 1
                    self.left_rotate(z.parent.parent)
            if z == self.root:
                break
        self.root.color = 0
            
    def insert(self, node):
        new_node = Node(node)
        new_node.leftChild = self.NULL
        new_node.rightChild = self.NULL
        y = None
        x = self.root
        while x != self.NULL:
            y = x
            if new_node.data < x.data:
                x = x.leftChild
            else:
                x = x.rightChild
        new_node.parent = y
        if y == None:
            self.root = new_node
        elif new_node.data < y.data:
            y.leftChild = new_node
        else:
            y.rightChild = new_node
        if new_node.parent is None:
            new_node.color = 0
            return
        if new_node.parent.parent is None:
            return
        self.fix_insert(new_node)
    
    def tree_minimum(self, x):
        while x.leftChild != self.NULL:
            x = x.leftChild
        return x
    
    def tree_successor(self, x):
        if x.rightChild != self.NULL:
            return self.tree_minimum(x.rightChild)
        y = x.parent
        while y != self.NULL and x == y.rightChild:
            x = y
            y = y.parent
        return y
    
    def rb_delete_fixup(self, x):
        while x != self.root and x.color == 0:
            if x == x.parent.leftChild:
                w = x.parent.rightChild
                if w.color == 1:
                    w.color = 0
                    x.parent.color = 1
                    self.left_rotate(x.parent)
                    w = x.parent.rightChild
                if w.leftChild.color == 0 and w.rightChild.color == 0:
                    w.color = 1
                    x = x.parent
                else:
                    if w.rightChild.color == 0:
                        w.leftChild.color = 0
                        w.color = 1
                        self.right_rotate(w)
                        w = x.parent.rightChild
                    w.color = x.parent.color
                    x.parent.color = 0
                    w.rightChild.color = 0
                    self.left_rotate(x.parent)
                    x = self.root
            else:
                w = x.parent.leftChild
                if w.color == 1:
                    w.color = 0
                    x.parent.color = 1
                    self.right_rotate(x.parent)
                    w = x.parent.leftChild
                if w.rightChild.color == 0 and w.leftChild.color == 0:
                    w.color = 1
                    x = x.parent
                else:
                    if w.leftChild.color == 0:
                        w.rightChild.color = 0
                        w.color = 1
                        self.left_rotate(w)
                        w = x.parent.leftChild
                    w.color = x.parent.color
                    x.parent.color = 0
                    w.leftChild.color = 0
                    self.right_rotate(x.parent)
                    x = self.root
        x.color = 0
                        
                        
    
    
    def delete(self, key):
        z = self.NULL
        node = self.root
        while node != self.NULL:
            if node.data == key:
                z = node

            if node.data <= key:
                node = node.rightChild
            else:
                node = node.leftChild

        if z == self.NULL:
            print("Cannot find key in the tree")
            return
        if z.leftChild == self.NULL or z.rightChild == self.NULL:
            y = z
        else:
            y = self.tree_successor(z)
        if y.leftChild != self.NULL:
            x = y.leftChild
        else:
            x = y.rightChild
        x.parent = y.parent
        if y.parent == self.NULL:
            self.root = x
        elif y == y.parent.leftChild:
            y.parent.leftChild = x
        else:
            y.parent.rightChild = x
        if y != z:
            z.data = y.data
        if y.color == 0:
            self.rb_delete_fixup(x)
        return y
            
    
    
if __name__ == '__main__':
    rbTree = RedBlackTree()
    rbTree.insert(33)
    rbTree.insert(13)
    rbTree.insert(53)
    rbTree.insert(11)
    rbTree.insert(21)
    rbTree.insert(41)
    rbTree.insert(61)
    rbTree.insert(15)
    rbTree.insert(31)
    rbTree.inorder_traversal()
    rbTree.delete(11)
    rbTree.inorder_traversal()