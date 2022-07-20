N = int(input())

for i in range(1, N + 1):
    if not N % i:
        print(i, end=' ')