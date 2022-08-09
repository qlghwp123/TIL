from pprint import pp, pprint

N, M = map(int, input().split())

# 열의 개수는 0 ~ N 까지 있어야하므로 N + 1 만큼 필요하다.
# 행의 개수는 0 ~ N 까지 있어야하므로 N + 1 만큼 필요하다.
# 인접 리스트도 결국 0 이 포함되므로 N + 1 만큼 필요하다.
mat = [[0] * (N + 1) for _ in range(N + 1)]
edges = [[] for _ in range(N + 1)]

for i in range(M):
    u, v = map(int, input().split())
    
    mat[u][v] = 1
    mat[v][u] = 1
    
    edges[u].append(v)
    # 무방향 그래프, 정렬이 안된 입력
    # 위와 조건들로 인하여 한 입력이 들어오면 
    # u, v를 바꿔서 한번 더 추가한다.
    edges[v].append(u)

pprint(mat)
pprint(edges)
