import sys
from collections import deque

input = sys.stdin.readline

w, h = 1, 1

while w and h:
    w, h = map(int, input().split())

    board = []

    for _ in range(h):
        board.append(list(map(int, input().split())))

    visited = [[False] * w for _ in range(h)]

    q = deque()
    q.append((0, 0))

    # i, j = 0, 0

    count = 0

    for i in range(h):
        for j in range(w):
            if not board[i][j] or visited[i][j]:
                continue

            while q:
                i, j = q.popleft()

                for k in range(-1, 2):
                    for l in range(-1, 2):
                        if -1 < i + k < h and -1 < j + l < w:
                            if (k or l) and board[i + k][j + l] and not visited[i + k][j + l]:
                                q.append((i + k, j + l))
                                visited[i][j] = True

            count += 1

    print(count)