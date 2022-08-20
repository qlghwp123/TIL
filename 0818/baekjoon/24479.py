# "방문 순서" 를 출력하는 것이 문제이다.
# 이 떄까지 문제를 제대로 이해하지 못했다.
# visited 에 boolean 대신 순서를 저장했다.
# DFS 에서 재귀가 스택보다 느리다는 일반화는 하지 않는 것이 좋겠다.
# 재귀로 구현한 코드가 내 코드보다 간결하며 빠르다.
# 메모리는 2배 이상 잡아 먹더라도 시간 면에서 모든 테스트 케이스에 있어서
# 100ms 차이가 나면 유의미한 차이이다.
# 참조 : https://www.acmicpc.net/source/47609216 (재귀로 구현)
# 참조 : https://www.acmicpc.net/board/view/97648 (3% 오류 반례) 
import sys

input = sys.stdin.readline

def dfs(start):
    global g, visited, N, M

    stack = [start]
    count = 1

    while stack:
        v = stack.pop()

        if not visited[v]:
            visited[v] = count
            count += 1

            for i in g[v]:
                if not visited[i]:
                    stack.append(i)


N, M, R = map(int, input().split())

g = {i:[] for i in range(1, N + 1)}
visited = [0] * (N + 1)

for _ in range(M):
    u, v = map(int, input().split())

    g[u].append(v)
    g[v].append(u)

for i in g:
    # DFS 구현 방법이 stack 이며, 문제 조건에 인접 정점은 오름차순으로 방문
    # 때문에 역방향으로 sort 이 필요하다.
    g[i].sort(reverse=True)

dfs(R)

print(*visited[1:], sep='\n')

# for i in g:
#     print(g[i])

# T1
# 5 5 1
# 1 4
# 1 2
# 2 3
# 2 4
# 3 4

# output 
# 1
# 2
# 3
# 4
# 0

# T2
# 6 4 1
# 2 3
# 1 4
# 1 5
# 4 6

# output
# 1
# 0
# 0
# 2
# 4
# 3