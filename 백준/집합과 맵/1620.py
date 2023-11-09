import sys

N, M = map(int, input().split())

dic_name ={}
dic_id ={}
for i in range(1, N+1):
    name = sys.stdin.readline().strip()
    dic_name[name] = i
    dic_id[i] = name

for i in range(M):
    id = sys.stdin.readline().strip()
    if id.isdigit() == True:
        print(dic_id[int(id)])
    else:
        print(dic_name[id])