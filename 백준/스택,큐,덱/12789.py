N = int(input())
T = list(map(int, input().split()))
stack = []
target = 1
while T:
    if T[0] == target:
        T.pop(0)
        target +=1
    else:
        stack.append(T.pop(0))
    
    while stack:
        if stack[-1] == target:
            stack.pop()
            target += 1
        else:
            break

if len(stack) == 0:
    print('Nice')
else:
    print('Sad')