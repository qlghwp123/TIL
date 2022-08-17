import sys

input = sys.stdin.readline

n, m = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

visited = [[False] * m for _ in range(n)]

def dfs(start):
    global board, visited, area_list

    stack = [start]
    area = 0

    while stack:
        x, y = stack.pop()

        if not visited[x][y]:
            # 넓이는 pop 한 것 중 방문하지 않은 것들이다.
            area += 1

            visited[x][y] = True

            for k in range(4):
                nx = x + dx[k]
                ny = y + dy[k]

                if -1 < nx < n and -1 < ny < m:
                    if board[nx][ny] and not visited[nx][ny]:
                        stack.append((nx, ny))

    return area


area_list = []

for i in range(n):
    for j in range(m):
        # 중복 방지를 위해 not visisted 를 넣어야한다.
        if board[i][j] and not visited[i][j]:
            area = dfs((i, j))
            area_list.append(area)

count = len(area_list)

if count:
    print(count, max(area_list), sep='\n')
else:
    # 출력 부분을 보고 0 하나 추가
    print(0, 0, sep='\n')