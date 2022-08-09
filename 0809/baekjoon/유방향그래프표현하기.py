from pprint import pp, pprint

N, M = map(int, input().split())

# 열의 개수는 0 ~ N 까지 있어야하므로 N + 1 만큼 필요하다.
# 행의 개수는 0 ~ N 까지 있어야하므로 N + 1 만큼 필요하다.
# 인접 리스트도 결국 0 이 포함되므로 N + 1 만큼 필요하다.
mat = [[0] * (N + 1) for _ in range(N + 1)]
edges = [[] for _ in range(N + 1)]

for i in range(M):
    u, v = map(int, input().split())
    
    # 유방향 그래프므로 같은 연산을 2번 할 필요가 없다.
    mat[u][v] = 1
    
    edges[u].append(v)

pprint(mat)
pprint(edges)
