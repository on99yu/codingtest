a, b = map(int, input().split())
# a,b = 5,2
result = 1
k =  1
for i in range(a, a-b, -1):
	result *= i
for i in range(b, 0,-1):
	k*=i
print(result//k)