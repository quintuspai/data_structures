class PostFixEval(object):
    """docstring for PostFixEval."""
    max_size = 20
    def __init__(self):
        super(PostFixEval, self).__init__()
        self.my_stack = []
        self.top = -1
    
    def push(self, val):
        if self.top == self.max_size - 1:
            print("Overflow\n")
        else:
            self.top += 1
            self.my_stack.append(val)
    
    def pop(self):
        if self.top == -1:
            print("Underflow\n")
            return -1
        else:
            val = self.my_stack.pop()
            self.top -= 1
            return val
    
    def evaluate(self, exp):
        for char in exp:
            if char.isdigit():
                self.push(char)
            else:
                op2 = self.pop()
                op1 = self.pop()
                if char == '+':
                    self.push(int(op1) + int(op2))
                if char == '-':
                    self.push(int(op1) - int(op2))
                if char == '*':
                    self.push(int(op1) * int(op2))
                if char == '/':
                    self.push(int(op1) / int(op2))
                if char == '%':
                    self.push(op1 % op2)
        print(self.pop())
    
if __name__ == "__main__":
    #postfix = input("Enter the postfix expression")
    postfix = '934*8+4/-'
    PostFixEval().evaluate(postfix)   