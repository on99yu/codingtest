while True:
    a ,b, c = map(int,input().split())
    if a == b == c == 0:
        break
    elif a == b== c:
        print('Equilateral')
    elif a+b <= c or b+c <= a or a+c <= b:
        print('Invalid')
    elif a == c or a == b or b == c:
        print('Isosceles')
    else:
        print('Scalene')