N = int(input())

P = list(map(int, input().split()))
P.sort()

ret = 0

for i in range(N):
    ret += P[i] * (N - i)

print(ret)