
while True:
    N = int(input())
    if N == -1:
        break
    divisor = [x for x in range(1, N) if N % x ==0]
    if sum(divisor) == N:
        print(N, ' = ', " + ".join(str(i) for i in divisor), sep="")
    else:
        print(N, "is NOT perfect.")