class Queue(object):
    max_size = 6
    queue = front = rear = None
    """docstring for Queue."""
    def __init__(self):
        super(Queue, self).__init__()
        self.front = self.rear = -1
        self.queue = [None] * self.max_size
    
    def insert(self, val):
        if self.rear == self.max_size - 1:
            print("Overflow \n")
        elif self.rear == -1 and self.front == -1:
            self.front = self.rear = 0
            self.queue[self.rear] = val
        else:
            self.rear = self.rear + 1
            self.queue[self.rear] = val
    
    def delete(self):
        if self.rear == -1 and self.front == -1:
            print("Underflow\n")
        else:
            val = self.queue[self.front]
            self.front = self.front + 1
            if self.front > self.rear:
                self.front = self.rear = -1
            print("{} deleted\n".format(val))
            
    def display(self):
        if self.rear == -1 and self.front == -1:
            print("Underflow\n")
        else:
            for i in range(self.front, self.rear + 1):
                print(self.queue[i])
        print('\n')
        
if __name__ == '__main__':
    q = Queue()
    q.insert(1)
    q.insert(2)
    q.insert(3)
    q.insert(4)
    q.insert(5)
    q.insert(6)
    q.display()
    q.delete()
    q.display()    