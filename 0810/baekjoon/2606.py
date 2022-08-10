def dfs(g, visited, R):
    # 재귀
    # if not visited[R]:
    #     visited[R] = True

    # for node in g[R]:
    #     if not visited[node]:
    #         dfs(g, visited, node)

    # 스택
    stack = [R]

    while stack:
        start = stack.pop()

        for node in g[start]:
            if not visited[node]:
                visited[node] = True
                stack.append(node)


N = int(input())

computer = int(input())

g = {i:[] for i in range(1, N + 1)}
for _ in range(computer):
    u, v = map(int, input().split())

    g[u].append(v)
    g[v].append(u)

visited = [False] * (N + 1)

dfs(g, visited, 1)

print(sum(visited) - 1)