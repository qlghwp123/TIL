# 해당 사이트를 참조했다.
# visited 를 사용하는 것을 제외하면 똑같았다.
# 촌수 계산 문제에서도 똑같이 visited[다음좌표] = visited[현재좌표] + 1 을 사용했었다.
# 아마 거리 계산을 위해 사용했을 것이다.
# https://codesyun.tistory.com/m/288

import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())

maze = []
for _ in range(N):
    maze.append(list(map(int, input()[:-1])))

visited = [[0] * M for _ in range(N)]

def bfs():
    q = deque()

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    i, j = 0, 0
    visited[i][j] = 1
    q.append((i, j, maze[i][j]))

    while True:
        i, j, path = q.popleft()

        # print(i, j, visited[i][j])

        if i == N - 1 and j == M - 1:
            print(visited[i][j])
            break

        for k in range(4):
            nx = i + dx[k]
            ny = j + dy[k]

            if -1 < nx < N and -1 < ny < M and maze[nx][ny] and not visited[nx][ny]:
                visited[nx][ny] = visited[i][j] + 1
                q.append((nx, ny, maze[nx][ny]))

bfs()