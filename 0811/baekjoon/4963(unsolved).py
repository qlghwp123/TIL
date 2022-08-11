import sys

input = sys.stdin.readline

w, h = 1, 1

def dfs():
    l


while w and h:
    l = []

    w, h = map(int, input().rstrip().split())

    for _ in range(h):
        l.append(list(map(int, input().rstrip().split())))

    visited = [False for i in range(h) for j in range(w) if l[i][j]]

    dfs()