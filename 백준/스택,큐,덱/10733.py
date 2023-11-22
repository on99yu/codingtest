import sys

K = int(sys.stdin.readline())
stack = []
for i in range(K):
    N = int(sys.stdin.readline())
    if N == 0:
        if len(stack) ==0:
            continue
        else:
            stack.pop()
    else:
        stack.append(N)
    
print(sum(stack))
