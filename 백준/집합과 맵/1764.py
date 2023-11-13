N, M = map(int, input().split())

N_dic = {input() : i for i in range(N)}
M_dic = {input() : i for i in range(M)}
count = 0
list = []
for i in N_dic:
    if i in M_dic:
        count +=1 
        list.append(i)

print(count)
for i in sorted(list):
    print(i)