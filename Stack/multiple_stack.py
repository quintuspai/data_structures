my_stack = [None] * 10
length_of_stack = len(my_stack)
topA = -1
topB = length_of_stack

def pushA(val):
    global topA, my_stack, topB
    if topA == topB - 1:
        print("Overflow A\n")
    else:
        topA = topA + 1
        my_stack[topA] = val

def popA():
    global topA, my_stack
    if topA == -1:
        print("Underflow A\n")
    else:
        val = my_stack[topA]
        topA = topA - 1
        print("{} popped from A\n".format(val))
            
def displayA():
    global topA, my_stack
    if topA == -1 :
        print("Underflow A\n")
    else:
        index = topA
        while index >= 0:
            print(my_stack[index])
            index = index - 1
    
def pushB(val):
    global topA, my_stack, topB
    if topB == topA + 1:
        print("Overflow B\n")
    else:
        topB = topB - 1
        my_stack[topB] = val
    
def popB():
    global topA, my_stack, topB
    if topB == length_of_stack:
        print("Underflow B\n")
    else:
        val = my_stack[topB]
        topB = topB + 1
        print("{} popped from B\n".format(val))
    
def displayB():
    if topB == length_of_stack:
        print("Underflow B\n")
    else:
        index = topB
        while index != length_of_stack:
            print(my_stack[index])
            index = index + 1
            
if __name__ == '__main__':
    pushA(0)
    pushA(1)
    pushA(2)
    pushA(3)
    pushA(4)
    pushB(11)
    pushB(12)
    pushB(13)
    pushB(14)
    pushB(15)
    popB()
    pushB(16)
    pushA(6)
    displayB()