import sys

input = sys.stdin.readline

w, h = 1, 1

def dfs(visited):
    pass


while w and h:
    l = []

    w, h = map(int, input().rstrip().split())

    for _ in range(h):
        l.append(list(map(int, input().rstrip().split())))

    visited = [(False, i, j) for i in range(h) for j in range(w) if l[i][j]]

    dfs(visited)