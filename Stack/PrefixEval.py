class PrefixEval(object):
    """docstring for PrefixEval."""
    def __init__(self):
        super(PrefixEval, self).__init__()
        self.my_stack = []
        
    def evaluate(self, exp):
        for char in exp[::-1]:
            if char.isdigit():
                self.my_stack.append(char)
            else:
                op1 = self.my_stack.pop()
                op2 = self.my_stack.pop()
                if char is '+':
                    res = int(op1) + int(op2)
                if char is '-':
                    res = int(op1) - int(op2)
                if char is '*':
                    res = int(op1) * int(op2)
                if char is '/':
                    res = int(op1) / int(op2)
                self.my_stack.append(res)
        print(self.my_stack.pop())
if __name__ == "__main__":
    #prefix_exp = input('Enter your prefix expression: ')
    prefix_exp = '+-927'
    PrefixEval().evaluate(prefix_exp)