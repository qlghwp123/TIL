# 주석 달린 부분들은 아래 사이트를 참조함.
# https://recordofwonseok.tistory.com/380

import sys

input = sys.stdin.readline


def dfs(g, visited, start):
    # 왜하는건지는 모르겠다...
    for node in g[start]:
        if visited[node] == -1:
            # 특히 이부분이 이해가 안된다. -> 자기 자신을 0으로 해서 재귀적으로 갈 때마다 이전 값에서 1씩 더해간다.
            # 즉 시작 ~ 해당 노드 간의 간선 길이와 같다.
            visited[node] = visited[start] + 1
            dfs(g, visited, node)


N = int(input())
start, end = map(int, input().split())
M = int(input())

g = {i:[] for i in range(1, N + 1)}
# 갈 수가 없을 경우 아예 -1 로 초기화한다.
visited = [-1] * (N + 1)

for _ in range(M):
    u, v = map(int, input().split())

    g[u].append(v)
    g[v].append(u)

for i in g:
    g[i].sort()

# 시작 점의 경우 0으로 초기화해서 출발한다.
visited[start] = 0

dfs(g, visited, start)

print(visited[end])