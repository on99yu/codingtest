N = int(input())
drawing_paper = [[0 for i in range(100)]for i in range(100)]

black =0
for i in range(N):
    w, h = map(int, input().split())
    for j in range(10):
        for k in range(10):
            drawing_paper[w+j][h+k] = 1

for i in range(100):
    for j in range(100):
        if drawing_paper[i][j] == 1:
            black += 1

print(black)