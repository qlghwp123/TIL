d  = [list(map(int,input().split())) for i in range(19)]
n = int(input())

for i in range(n):
    x, y = map(int, input().split())

    for j in range(19):
        for k in range(19):
            if j != x-1 or k != y-1:
                d[x-1][k] = 0 if d[x-1][k] == 1 else 1
                d[j][y-1] = 0 if d[j][y-1] == 1 else 1

for i in range(19):
    for j in range(19):
        print(d[i][j], end=' ')
    print()