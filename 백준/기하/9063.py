N =int(input())
width = []
height= []
for i in range(N):
    a, b = map(int, input().split())
    width.append(a)
    height.append(b)
if len(width) == 1 and len(height) ==1:
    print(0)
else: 
    print((max(width)-min(width))*(max(height)-min(height)))