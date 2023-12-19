N, M = map(int, input().split())
A = list(map(int,input().split()))
S = [0]*(N+1)
S[1] = A[0]

for i in range(2, N+1):
    S[i] = S[i-1]+A[i-1]

for i in range(M):
    f, l = map(int, input().split())
    print(S[l]-S[f-1])

