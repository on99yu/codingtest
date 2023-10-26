L = [['' for i in range(15)]for row in range(5)]
word = ''
for i in range(5):
    W = input()
    for j in range(len(W)):
        L[i][j] = W[j]
for i in range(15):
    word = word + L[0][i]+L[1][i]+L[2][i]+L[3][i]+L[4][i]

print(word)
