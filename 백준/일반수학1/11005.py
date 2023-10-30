digit_number = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

N, digit = map(int, input().split())
res = ''
while N != 0 :
    res += str(digit_number[N%digit])
    N = N // digit

print(res[::-1])    

    

