class PostFixEval(object):
    """docstring for PostFixEval."""
    def __init__(self):
        super(PostFixEval, self).__init__()
        self.my_stack = []
        self.top = -1
    
    def evaluate(self, exp):
        for char in exp:
            if char.isdigit():
                self.my_stack.push(char)
            else:
                op2 = self.my_stack.pop()
                op1 = self.my_stack.pop()
                if char == '+':
                    self.push(int(op1) + int(op2))
                if char == '-':
                    self.push(int(op1) - int(op2))
                if char == '*':
                    self.push(int(op1) * int(op2))
                if char == '/':
                    self.push(int(op1) / int(op2))
                if char == '%':
                    self.my_stack.push(op1 % op2)
        print(self.my_stack.pop())
    
if __name__ == "__main__":
    #postfix = input("Enter the postfix expression")
    postfix = '934*8+4/-'
    PostFixEval().evaluate(postfix)   