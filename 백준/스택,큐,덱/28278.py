import sys

N = int(input())
stack =[]

for i in range(N):
    c = sys.stdin.readline().split()
    if c[0] == '1':
        stack.append(c[1])
    elif c[0] == '2':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())
    elif c[0] == '3':
        print(len(stack))
    elif c[0] == '4':
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif c[0] == '5':
        if (len(stack)) == 0:
            print(-1)
        else:
            print(stack[-1])
        