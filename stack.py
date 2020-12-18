n = int(input("Enter size : "))
top = -1
stk = []
for i in range(n):
    stk.append(0)

def push():
    global top
    if top != n-1:
        top += 1
        x = int(input("Enter Element to be pushed in the stack : "))
        stk[top] = x
        print(stk[top]," pushed at ",top)
    else:
        print("Stack Overflow")


def pop():
    global top
    if top != -1:
        print(stk[top]," popped from ",top)
        top -= 1
    else:
        print("Stack Underflow")

def traverse():
    global top
    print("Elements are : ",end=":--  ")
    for i in reversed(range(top+1)):
        print(stk[i], end=" ")
    print("\n")




while True:
    c = int(input("1. Push\n2. Pop\n3. Traverse\nAny other key to Quit\n"))
    if c == 1:
        push()
    elif c == 2:
        pop()
    elif c == 3:
        traverse()
    else:
        break





























