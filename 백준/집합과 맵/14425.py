N, M = map(int, input().split())
words =[]
count = 0
dic = {input() : i for i in range(N)}
for i in range(M):
    word = input()
    words.append(word)

for i in words:
    if i in dic:
        count += 1
print(count)