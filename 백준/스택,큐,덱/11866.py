from collections import deque

N, K = map(int, input().split())

queue = deque([i for i in range(1, N+1)])
stack =[]
i = 0
while True:
    if len(queue) == 0:
        break
    queue.append(queue.popleft())
    i += 1
    if i == K:
        stack.append(queue.pop())
        i = 0
print('<', end="")
for i in range(len(stack)):
    if i+1 == len(stack):
        print(stack[i], end="")
        break
    print(stack[i], end=", ")
print('>')
