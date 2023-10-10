N, M = map(int, input().split())

list1 = [list(map(int, input().split())) for _ in range(N) ]    
list2 = [list(map(int, input().split())) for _ in range(N) ] 
list3 = [[0]*M for _ in range(N)]
for i in range(N):
    for j in range(M):
        list3[i][j] = list1[i][j] + list2[i][j]

for i in range(N):
    for j in range(M):
        print(list3[i][j], end=" ")
    print()

