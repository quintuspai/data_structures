class MultipleQueue(object):
    multiple_queue = None
    max_size = 10
    frontA = rearA = frontB = rearB = None
    """docstring for MultipleQueue."""
    def __init__(self):
        super(MultipleQueue, self).__init__()
        self.rearA = self.frontA = -1
        self.rearB = self.frontB = self.max_size 
        self.multiple_queue = [None] * self.max_size
    
    def insertA(self, val):
        if self.rearA == self.rearB - 1:
            print("Overflow A\n")
        elif self.frontA == -1 and self.rearA == -1:
            self.frontA = self.rearA = 0
            self.multiple_queue[self.rearA] = val
        else:
            self.rearA = self.rearA + 1
            self.multiple_queue[self.rearA] = val
            
    def deleteA(self):
        if self.frontA == -1 and self.rearA == -1:
            print("Underflow A\n")
        else:
            val = self.multiple_queue[self.frontA]
            self.frontA = self.frontA + 1
            if self.frontA > self.rearA:
                self.frontA = self.rearA = -1
            print('{} is deleted from A\n'.format(val))
            
    def display(self):
        if self.frontA == -1 and self.rearA == -1:
            print("Underflow A\n")
        else:
            for i in range(self.frontA, self.rearA + 1):
                print(self.multiple_queue[i])
            print("\n")
    
    def insertB(self, val):
        if self.rearB == self.rearA + 1:
            print("Overflow B\n")
        elif self.frontB == self.max_size and self.rearB == self.max_size:
            self.frontB = self.rearB = self.max_size - 1
            self.multiple_queue[self.rearB] = val
        else:
            self.rearB = self.rearB - 1
            self.multiple_queue[self.rearB] = val
    
    def deleteB(self):
        if self.frontB == self.max_size and self.rearB == self.max_size:
            print("UnderflowB\n")
        else:
            val = self.multiple_queue[self.frontB]
            self.frontB = self.frontB - 1
            if self.frontB < self.rearB:
                self.frontB = self.rearB = self.max_size
            print("{} is deleted from B\n".format(val))
            
    def displayB(self):
        if self.frontB == self.max_size and self.rearB == self.max_size:
            print("UnderflowB\n")
        else:
            front = self.frontB
            rear = self.rearB
            while front >= rear:
                print(self.multiple_queue[front])
                front = front - 1

if __name__ == '__main__':
    q = MultipleQueue()
    q.insertA(1)
    q.insertA(2)
    q.insertA(3)
    q.insertA(4)
    q.insertA(5)
    q.display()
    q.insertB(11)
    q.insertB(12)
    q.insertB(13)
    q.insertB(14)
    q.insertB(15)