import time, sys

start = time.time()

M, N = map(int, sys.stdin.readline().split())

l = [ 1 for i in range(2, N+1)]
i = 2   

while i * i <= N:

    for j in range(N):
        if not j % i and j != i:
            print(j)
            l[j] = 0

    i += 1


for i in range(2, N+1):
    if l[i]:
        print(i)

end = time.time()

print(f"{end - start:.5f} sec")