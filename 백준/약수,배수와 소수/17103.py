T = int(input())

def makeprimelist(x):
    a = [True]*(x+1)
    for i in range(2, int(x**0.5)+1):
        if a[i] == True:
            for j in range(i+i, x+1, i):
                a[j] = False
    return a

primelist = makeprimelist(1000000)
for i in range(T):
    N = int(input())
    count = 0
    for j in range(2, (N//2)+1):
        if  primelist[j] and primelist[N-j]:
            count +=1
    print(count)


