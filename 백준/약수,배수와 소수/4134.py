T = int(input())

def isprime(x):
    i = 2
    if x == 0 or x == 1:
        return False
    for i in range(2, int(x**0.5)+1):
        if x % i == 0:
            return False
    return True
            

for i in range(T):
    n = int(input())
    while True:
        if isprime(n):
            break
        else:
            n+=1
    print(n)