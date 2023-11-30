import sys
from collections import deque
N = int(input())
Deque = deque([])
for i in range(N):
    C = sys.stdin.readline().strip().split()
    L = len(Deque)
    if C[0] == '1':
        Deque.appendleft(C[1])
    elif C[0] == '2':
        Deque.append(C[1])
    elif C[0] == '3':
        print(-1 if L == 0 else Deque.popleft())
    elif C[0] == '4':
        print(-1 if L == 0 else Deque.pop())
    elif C[0] == '5':
        print(L)
    elif C[0] == '6':
        print(-1 if L == 0 else 0)
    elif C[0] == '7':
        print(-1 if L == 0 else Deque[0])
    elif C[0] == '8':
        print(-1 if L == 0 else Deque[-1])
