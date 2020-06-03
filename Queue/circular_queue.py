class CircularQueue(object):
    max_size = 5
    circular_queue = front = rear = None
    """docstring for CircularQueue."""
    def __init__(self):
        super(CircularQueue, self).__init__()
        self.front = self.rear = -1
        self.circular_queue = [None] * self.max_size
    
    def insert(self, val):
        if self.front == 0 and self.rear == self.max_size - 1:
            print("Overflow\n")
        elif self.front == -1 and self.rear == -1:
            self.rear = self.front = 0
            self.circular_queue[self.rear] = val
        elif self.front != 0 and self.rear == self.max_size - 1:
            self.rear = 0
            self.circular_queue[self.rear] = val
        else:
            self.rear = self.rear + 1
            self.circular_queue[self.rear] = val
    
    def delete(self):
        if self.rear == -1 and self.rear == -1:
            print("Underflow\n")
        elif self.rear == self.front:
            val = self.circular_queue[self.front]
            self.rear = self.front = -1
            print('{} is deleted\n'.format(val))
        else:
            val = self.circular_queue[self.front]
            print('{} is deleted\n'.format(val))
            if self.front == self.max_size - 1:
                self.front = 0
            else:
                self.front = self.front + 1
    
    def display(self):
        if self.rear == -1 and self.front == -1:
            print("Underflow \n")
        else:
            if self.front < self.rear or self.front == self.rear:
                for i in range(self.front, self.rear + 1):
                    print(self.circular_queue[i])
            else:
                for i in range(self.front,self.max_size):
                    print(self.circular_queue[i])
                for i in range(0, self.rear):
                    print(self.circular_queue[i])
            print("\n")
                    
if __name__ == '__main__':
    cq = CircularQueue()
    cq.insert(1)
    cq.insert(2)
    cq.insert(3)
    cq.insert(4)
    cq.insert(5)
    cq.display()
    cq.insert(6)
    #cq.display()