N = int(input())
number = sorted(list(map(int, input().split())))
M = int(input())
check_num = list(map(int, input().split()))

dic={}
for i in number:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1

for i in check_num:
    if i in dic:
        print(dic[i], end=" ")
    else:
        print(0,end=" ")