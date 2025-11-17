import sys
stack = []
top = -1
a = int(input())
for _ in range(a):
    b = sys.stdin.readline().split()
    if b[0] == "push":
        stack.append(b[1])
        top+=1
    elif b[0] == "top":
        if top<0:
            print(-1)
        else:
            print(stack[top])
    elif b[0] == "empty":
        if top >= 0:print(0)
        else:print(1)
    elif b[0] == "pop":
        if top>-1:
            print(stack.pop())
            top-=1
        else: print(-1)
    elif b[0] == "size":
        print(len(stack))