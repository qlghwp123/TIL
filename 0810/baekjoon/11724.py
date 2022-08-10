import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

def dfs(g, visited, start):
    if not visited[start]:
        visited[start] = True
    else:
        return 0
  
    for node in g[start]:
        if not visited[node]:
            dfs(g, visited, node)
    
    return 1

N, M = map(int, input().split())

g = {i:[] for i in range(1, N + 1)}
visited = [False] * (N + 1)

for _ in range(M):
    u, v = map(int, input().split())

    g[u].append(v)
    g[v].append(u)

count = 0
check = [False] + [True for i in range(N)]
for i in range(1, N + 1):
    if visited != check:
        count += dfs(g, visited, i)
    else:
        break

print(count)

# 아래 코드가 더 깔끔하다.
# https://www.acmicpc.net/source/47462290

# import sys

# input = sys.stdin.readline


# def dfs(node):
#     visited[node] = True
#     for j in graph[node]:
#         if not visited[j]:
#             dfs(j)


# N, M = map(int, input().split())
# visited = [False]*(N+1)

# graph = [[] for _ in range(N+1)]
# for _ in range(1, M+1):
#     u, v = map(int, input().split())
#     graph[u].append(v)
#     graph[v].append(u)


# ans = 0
# for k in range(1, N+1):
#     if not visited[k]:
#         dfs(k)
#         ans += 1

# print(ans)