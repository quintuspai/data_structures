class Node(object):
    nodes = None
    flag = 0
    """docstring for Node."""
    def __init__(self, data, leftChild = None, rightChild = None):
        super(Node, self).__init__()
        self.data = data
        self.leftChild = leftChild
        self.rightChild = rightChild
    
    def get_data(self):
        return self.data
    
    def get_leftChild(self):
        return self.leftChild
    
    def get_rightChild(self):
        return self.rightChild
    
    def set_data(self, new_data):
        self.data = new_data
    
    def set_leftChild(self, new_leftChild):
        self.leftChild = new_leftChild
    
    def set_rightChild(self, new_rightChild):
        self.rightChild = new_rightChild


class Tree(object):
    """docstring for Tree."""
    def __init__(self):
        super(Tree, self).__init__()
        self.root = None
    
    def insert_node(self, data):
        new_node = Node(data)
        if self.root is None:
            self.root = new_node
        else:
            parentptr = None
            currentnode = self.root
            while currentnode != None:
                parentptr = currentnode
                if data < currentnode.get_data():
                    currentnode = currentnode.get_leftChild()
                else:
                    currentnode = currentnode.get_rightChild()
            if data < parentptr.get_data():
                parentptr.set_leftChild(new_node)
            else:
                parentptr.set_rightChild(new_node)
    
    def perform_delete(self, root, val):
        if root is None:
            return root
        if val < root.get_data():
            root.leftChild = self.perform_delete(root.get_leftChild(), val)
        elif val > root.get_data():
            root.rightChild = self.perform_delete(root.get_rightChild(), val)
        else:
            if root.get_leftChild() is None:
                temp = root.get_rightChild()
                root = None
                return temp
            if root.get_rightChild() is None:
                temp = root.get_leftChild()
                root = None
                return temp
            temp = self.retrieve_smallest_node(root.get_rightChild())
            root.set_data(temp.get_data())
            root.set_rightChild(self.perform_delete(root.get_rightChild(), temp.get_data()))
        return root
            
    def delete_node(self, val):
        self.perform_delete(self.root, val)
    
    def perform_preorder(self, root):
        if root != None:
            print(root.get_data(), end = ' ')
            self.perform_preorder(root.get_leftChild())
            self.perform_preorder(root.get_rightChild())
    
    def preorder_traversal(self):
        self.perform_preorder(self.root)
        print("\n")
    
    def perform_inorder(self, root):
        if root != None:
            self.perform_inorder(root.get_leftChild())
            print(root.get_data(), end = ' ')
            self.perform_inorder(root.get_rightChild())
    
    def inorder_tarversal(self):
        self.perform_inorder(self.root)
        print("\n")
            
    def perform_postorder(self, root):
        if root != None:
            self.perform_postorder(root.get_leftChild())
            self.perform_postorder(root.get_rightChild())
            print(root.get_data(), end = ' ')
    
    def postorder_traversal(self):
        self.perform_postorder(self.root)
        print("\n")
    
    def retrieve_smallest_node(self, root):
        if root == None or root.get_leftChild() == None:
            return root.get_data()
        else:
            return self.retrieve_smallest_node(root.get_leftChild())
    
    def find_smallest_node(self):
        print("{} is the smallest node\n".format(self.retrieve_smallest_node(self.root)))
        
    def retrieve_largest_node(self, root):
        if root == None or root.get_rightChild() == None:
            return root.get_data()
        else:
            return self.retrieve_largest_node(root.get_rightChild())
    
    def find_largest_node(self):
        print("{} is the largest node\n".format(self.retrieve_largest_node(self.root)))
        
    def compute_tree_height(self, root):
        if root == None:
            return 0
        else:
            leftHeight = self.compute_tree_height(root.get_leftChild())
            rightHeight = self.compute_tree_height(root.get_rightChild())
            return max(leftHeight, rightHeight) + 1
    
    def find_height(self):
        print("{} is the height of the tree\n".format(self.compute_tree_height(self.root)))
    
    def compute_total_nodes(self, root):
        if root == None:
            return 0
        else:
            return ((self.compute_total_nodes(root.get_leftChild())) + (self.compute_total_nodes(root.get_rightChild())) + 1)
    
    def find_total_nodes(self):
        print("{} is the totla number of nodes\n".format(self.compute_total_nodes(self.root)))
    
    def compute_external_nodes(self, root):
        if root == None:
            return 0
        elif root.get_leftChild() == None and root.get_rightChild() == None:
            return 1
        else:
            return (self.compute_external_nodes(root.get_leftChild()) + self.compute_external_nodes(root.get_rightChild()))
    
    def total_external_nodes(self):
        print("{} is the total number of external nodes\n".format(self.compute_external_nodes(self.root)))

    def compute_internal_nodes(self, root):
        if root == None:
            return 0
        elif root.get_leftChild() == None and root.get_rightChild() == None:
            return 0
        else:
            return self.compute_internal_nodes(root.get_leftChild()) + self.compute_internal_nodes(root.get_rightChild()) + 1
 
    def total_internal_nodes(self):
        print("{} is the total number of internal nodes\n".format(self.compute_internal_nodes(self.root)))
        
    def perform_mirror_image(self, root):
        if root != None:
            self.perform_mirror_image(root.get_leftChild())
            self.perform_mirror_image(root.get_rightChild())
            temp = root.get_leftChild()
            root.set_leftChild(root.get_rightChild())
            root.set_rightChild(temp)    
    
    def mirror_image(self):
        self.perform_mirror_image(self.root)
    
    def compute_search(self, root, val):
        if root == None:
            print("Not found\n")
        elif root.get_data() == val:
            print("Found\n")
        else:
            if val < root.get_data():
                self.compute_search(root.get_leftChild(), val)
            else:
                self.compute_search(root.get_rightChild(), val)
        
    def search_node(self, val):
        self.compute_search(self.root, val)


if __name__ == '__main__':
    bst = Tree()
    bst.insert_node(50)
    bst.insert_node(30)
    bst.insert_node(20)
    bst.insert_node(40)
    bst.insert_node(70)
    bst.insert_node(60)
    bst.insert_node(80)
    bst.inorder_tarversal()
    bst.delete_node(20)
    bst.inorder_tarversal()
    #bst.insert_node(20)
    #bst.inorder_tarversal()