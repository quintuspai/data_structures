class Stack(object):
    my_stack = None
    top = None
    """docstring for Stack."""
    def __init__(self):
        super(Stack, self).__init__()
        self.my_stack = []
        self.top = -1
    
    def push(self):
        val = int(input('Enter the number : '))
        self.top = self.top + 1
        self.my_stack.append(val)
    
    def pop(self):
        if self.top == -1:
            print("Stack is empty")
        else:
            val = self.my_stack.pop(self.top)
            self.top = self.top - 1
            print('The value deleted was : {}'.format(val))
    
    def display(self):
        if self.top == -1:
            print("Stack is empty")
        else:
            i = self.top
            for _ in range(len(self.my_stack)):
                print(self.my_stack[i])
                i = i - 1
    
if __name__ == '__main__':
    s = Stack()
    choice = int(input("1:Push 2:Pop 3:Display 4:Exit : "))
    while choice != 4:
        if choice == 1:
            s.push()
        if choice == 2:
            s.pop()
        if choice == 3:
            s.display()
        choice = int(input("1:Push 2:Pop 3:Display 4:Exit : "))
    