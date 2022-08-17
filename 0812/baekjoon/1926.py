import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().rstrip().split())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
    global board, visited, count, area_list

    q = deque()

    for i in range(n):
        for j in range(m):
            if board[i][j] and not visited[i][j]:
                area = 0

                q.append((i, j))

                while q:
                    x, y = q.popleft()

                    area += 1

                    visited[x][y] = True

                    for k in range(4):
                        nx = x + dx[k]
                        ny = y + dy[k]

                        if -1 < nx < n and -1 < ny < m:
                            if board[nx][ny] and not visited[nx][ny]:
                                q.append((nx, ny))

                area_list.append(area)
                count += 1

board = []
visited = [[False] * m for _ in range(n)]

for __ in range(n):
    board.append(list(map(int, input().rstrip().split())))

count = 0
area_list = [] 

bfs()

print(count, max(area_list) if area_list else 0, sep='\n')