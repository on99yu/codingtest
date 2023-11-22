import sys

T= int(sys.stdin.readline())

for i in range(T):
    V = input()
    stack=[]
    for j in V:
        if j == '(':
            stack.append(j)
        elif j ==')':
            if len(stack) == 0:
                print('NO')
                break
            else:
                stack.pop()
    else: 
        if len(stack) == 0:
            print('YES')
        else:
            print('NO')
    

        
