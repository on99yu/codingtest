n = int(input())
dic ={}
for i in range(n):
    name, state = map(str, input().split())
    if state == 'enter':
        dic[name] = state
    else:
        del dic[name]
        
dic = sorted(dic.items(), reverse=True)
for i in dic:
    if i[1] =='enter':
        print(i[0])
    