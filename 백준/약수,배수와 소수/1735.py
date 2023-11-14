from math import gcd

A, B = map(int, input().split())
C ,D = map(int, input().split())

mom = B*D
son = A*D + C*B
gcd = gcd(mom,son)
mom = mom//gcd
son = son//gcd
print(son, mom)