class InfixToPrefix(object):
    """docstring for InfixToPrefix."""
    max_size = 20
    def __init__(self):
        super(InfixToPrefix, self).__init__()
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
            return -1
        else:
            val = self.my_stack.pop(self.top)
            self.top -= 1
            return val
    
    def getPriority(self, op):
        if op == '/' or op == '*' or op == '%':
            return 1
        if op == '+' or op == '-':
            return 0
        
    def reverse(self, exp):
        rev = ''
        for char in exp:
            if char == "(":
                char = ")"
            if char == ")":
                char = "("
            rev = char + rev
        return rev
    
    def infixtoprefix(self, exp):
        target = ''
        for char in exp:
            if char.isdigit() or char.isalpha():
                target += char
            elif char in '+-*/%':
                while self.top != -1 and self.my_stack[self.top] != "(" and (self.getPriority(self.my_stack[self.top]) > self.getPriority(char)):
                    target += self.pop()
                self.push(char)
            elif char is "(":
                self.push(char)
            elif char is ")":
                temp = self.pop()
                while temp != "(":
                    target += temp
                    temp = self.pop()
        while self.top != -1:
            if self.my_stack[self.top] is '(':
                self.pop()
            else:
                target += self.pop()
        return target
                            
                    
if __name__ == '__main__':
    #exp = input("Enter your infix expression: ")
    exp = '(A+B)*C'
    res = InfixToPrefix().reverse(exp)
    a = InfixToPrefix().infixtoprefix(res)
    f = InfixToPrefix().reverse(a)
    print(f)