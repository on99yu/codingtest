from math import gcd

N = int(input())
trees = [int(input()) for _ in range(N)]
dif_list = []
count = 0

def gcd_N(arr):
    gcd_n = arr[0]
    for item in arr:
        gcd_n = gcd(gcd_n, item)
    return gcd_n

for i in range(1, N):
    dif_list.append(trees[i] - trees[i-1])

GCD = gcd_N(dif_list)

for i in dif_list:
    count += i // GCD - 1

print(count)