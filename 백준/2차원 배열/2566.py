N =9 
arr = []
max = 0
coordinates = [0, 0] 
for i in range(N):
    arr.append(list(map(int, input().split())))

for i in range(N):
    for j in range(N):
        if arr[i][j] >= max:
            max = arr[i][j]
            coordinates[0] = i+1
            coordinates[1] = j+1

print(max)
print(coordinates[0],coordinates[1])