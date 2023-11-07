N = int(input())
NL = list(map(int, input().split()))
M = int(input())
ML = list(map(int, input().split()))

dic ={}
for i in range(len(NL)):
    dic[NL[i]] = 0 

for i in ML:
    if i in dic:
        print(1, end=" ")
    else:
        print(0, end=" ")
