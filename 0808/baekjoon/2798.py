N, M = map(int, input().split())

cards = list(map(int, input().split()))

ret = 0
for i in range(N - 2):
    for j in range(i + 1, N - 1):
        for k in range(j + 1, N):
            if ret < cards[i] + cards[j] + cards[k] <= M:
                ret = cards[i] + cards[j] + cards[k]
    if ret == M:
        break

print(ret)