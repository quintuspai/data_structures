class InfixToPostFix(object):
    Max_size = 20
    def __init__(self):
        super(InfixToPostFix, self).__init__()
        self.my_stack = [None] * self.Max_size
        self.top = -1
    
    def push(self, val):
        if self.top == self.Max_size - 1:
            print("Overflow\n")
        else:
            self.top = self.top + 1
            self.my_stack[self.top] = val
    
    def pop(self):
        if self.top == -1:
            print("Underflow\n")
        else:
            val = self.my_stack[self.top]
            self.top = self.top - 1
        return val
    
    def getPriority(self, op):
        if op == '/' or op == '*' or op == '%':
            return 1
        if op == '+' or op == '-':
            return 0
    
    def convert(self, exp):
        target = ''
        for char in exp:
            if char.isdigit() or char.isalpha():
                target += char
            elif char in '+-/*%':
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
            if self.my_stack[self.top] is "(":
                self.pop()
            else:
                target += self.pop()
        print(target)        
        
            
if __name__ == "__main__":
    itp = InfixToPostFix()
    #infix = input("Enter infix expression: ")
    infix = "A-(B/C+(D%E*F)/G)*H"
    itp.convert(infix)
        