N = int(input())

for i in range(N):
    num = int(input())
    a = num // 25
    num = num%25
    b = num // 10
    num = num%10
    c = num // 5
    num = num%5
    d = num // 1
    print(a, b, c, d)