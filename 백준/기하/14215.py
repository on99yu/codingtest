a, b, c = map(int, input().split())

if c >= a+b:
    print(a+b+(a+b-1))
elif b >= a+c:
    print(a+c+(a+c-1))
elif a >= b+c:
    print(b+c+(b+c-1))
else:
    print(a+b+c)