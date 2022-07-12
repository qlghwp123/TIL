h, w = map(int, input().split())
n = int(input())

b = [ [0 for i in range(w)] for i in range(h)]

for i in range(n):
    l, d, x, y = map(int,input().split())

    for i in range(l):
        if not d:
            b[x - 1][y - 1 + i] = 1
        else:
            b[x - 1 + i][y - 1] = 1

for i in range(h):
    for j in range(w):
        print(b[i][j], end=' ')
    print()