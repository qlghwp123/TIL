# 참조
# https://latte-is-horse.tistory.com/305
# 사실 봤을 때, 내가 짠 코드랑 다른 점은 global 이랑 visited 차이뿐이였다.

import sys
from collections import deque

input = sys.stdin.readline

w, h = 1, 1

def bfs():
    # 사이트 보고 참조함.
    global board, visited, w, h, count

    q = deque()
    
    for i in range(h):
        for j in range(w):
            if not visited[i][j] and board[i][j]:
                q.append((i, j))
            else:
                continue

            while q:
                x, y = q.popleft()

                if not visited[x][y]:
                    visited[x][y] = True

                    for k in range(-1, 2):
                        for l in range(-1, 2):
                            if (k or l) and -1 < x + k < h and -1 < y + l < w:
                                if board[x + k][y + l]:
                                    q.append((x + k, y + l))

            count += 1

    print(count)
    


while w and h:
    board = []

    w, h = map(int, input().rstrip().split())

    if not w and not h:
        break

    for _ in range(h):
        board.append(list(map(int, input().rstrip().split())))

    visited = [[False] * w for _ in range(h)]

    count = 0

    bfs()