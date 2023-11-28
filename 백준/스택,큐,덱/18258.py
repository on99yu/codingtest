import sys
from collections import deque
N = int(input())
queue = deque([])
for i in range(N):
    S = sys.stdin.readline().split()
    if S[0] == 'push':
        queue.append(S[1])
    elif S[0] == 'pop':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue.popleft())
    elif S[0] == 'size':
        print(len(queue))
    elif S[0] == 'empty':
        if len(queue) == 0:
            print(1)
        else:
            print(0)
    elif S[0] == 'front':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])
    elif S[0] == 'back':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[-1])