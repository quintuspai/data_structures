class Deque(object):
    deque = None
    left = right = None
    max_size = 6
    """docstring for Deque."""
    def __init__(self):
        super(Deque, self).__init__()
        self.left = self.right = -1
        self.deque = [None] * self.max_size
    
    def insert_left(self, val):
        if (self.left == 0 and self.right == self.max_size - 1) or (self.left == self.right + 1):
            print("Overflow\n")
        elif self.left == -1 and self.right == -1:
            self.left = self.right = 0
            self.deque[self.left] = val
        else:
            if self.left == 0:
                self.left = self.max_size - 1
            else:
                self.left = self.left - 1
            self.deque[self.left] = val                
    
    def insert_right(self, val):
        if (self.left == 0 and self.right == self.max_size - 1) or (self.left == self.right + 1):
            print("Overflow\n")
        elif self.left == -1 and self.right == -1:
            self.left = self.right = 0
            self.deque[self.right] = val
        else:
            if self.right == self.max_size - 1:
                self.right = 0
            else:
                self.right = self.right + 1
            self.deque[self.right] = val
    
    def delete_left(self):
        if self.left == -1 and self.right == -1:
            print("Undeflow\n")
        if self.left == self.right:
            val = self.deque[self.left]
            self.left = self.right = -1
            print("{} is deleted left\n".format(val))
        else:
            val = self.deque[self.left]
            print("{} is deleted from left\n".format(val))
            if self.left == self.max_size - 1:
                self.left = 0
            else:
                self.left = self.left + 1
    
    def delete_right(self):
        if self.left == -1 and self.right == -1:
            print("Underflow\n")
        if self.left == self.right:
            val = self.deque[self.right]
            self.right = self.left = -1
            print('{} deleted from right\n'.format(val))
        else:
            val = self.deque[self.right]
            print("{} deleted from right\n".format(val))
            if self.right == 0:
                self.right = self.max_size - 1
            else:
                self.right = self.right - 1
    
    def display(self):
        if self.left == -1 and self.right == -1:
            print("Underflow\n")
        else:
            front = self.left
            rear = self.right
            if front <= rear:
                while front <= rear:
                    print(self.deque[front])
                    front = front + 1
            else:
                while front <= self.max_size - 1:
                    print(self.deque[front])
                    front = front + 1
                front = 0
                while front <= rear:
                    print(self.deque[front])
                    front = front + 1
            print("\n")


if __name__ == '__main__':
    d = Deque()
    d.insert_left(0)
    d.insert_left(1)
    d.display()
    d.delete_right()
    d.display()
    
    
    