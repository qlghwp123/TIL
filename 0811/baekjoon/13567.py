import sys

input = sys.stdin.readline

M, n = map(int, input().rstrip().split())

i, j = 0, 0

# 왼쪽은 turn -= 1, 오른쪽은 turn += 1
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

turn = 0

for _ in range(n):
    cmd, val = input().rstrip().split()

    val = int(val)

    if cmd == "TURN":
        turn = (turn + 1) % 4 if val else (turn - 1) % 4
    else:
        i, j = i + val * dx[turn], j + val * dy[turn]

        if not (-1 < i <= M) or not (-1 < j <= M):
            break

if not (-1 < i <= M) or not (-1 < j <= M):
    print(-1)
else:
    print(i, j)