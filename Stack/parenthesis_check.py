max_size = 10
equation = [None] * max_size
top = -1

def push(val):
    global top, equation
    if top == max_size - 1:
        print('Overflow\n')
    else:
        top = top + 1
        equation[top] = val
        
def pop():
    global top, equation
    if top == -1:
        print('Underflow\n')
    else:
        val = equation[top]
        top = top - 1
        return val

if __name__ == '__main__':
    flag = 1
    input_equation = input("Enter the equation : ")
    for ch in input_equation:
        if ch == '{' or ch == '[' or ch == '(':
            push(ch)
        if ch == '}' or ch == ']' or ch == ')':
            if top == -1:
                flag = 0
            else:
                temp = pop()
                if ch == '}' and (temp == '(' or temp == '['):
                    flag = 0
                if ch == ')' and (temp == '[' or temp == '{'):
                    flag = 0
                if ch == ']' and (temp == '{' or temp == '('):
                    flag = 0
    if top >= 0:
        flag = 0
    if flag == 1:
        print("valid")
    else:
        print("invalid")            
            