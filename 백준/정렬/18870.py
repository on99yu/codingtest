N = int(input())
List = list(map(int, input().split()))

com_l = sorted(list(set(List)))

dic = {com_l[i] : i for i in range(len(com_l))}

for i in List:
    print(dic[i], end=" ")