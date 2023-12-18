from collections import deque
N = int(input())
Deque = deque(enumerate(map(int, input().split())))
stack = []

while Deque:
    idx, bal = Deque.popleft()
    stack.append(idx+1)
    if bal > 0:
        for i in range(bal-1):
            Deque.rotate(-1)
    if bal < 0:
        for i in range(abs(bal)):
            Deque.rotate(1)
        
for i in stack:
    print(i, end=" ")