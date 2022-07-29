import sys

N, M = map(int, sys.stdin.readline().split())

n = set()
m = set()
for i in range(N + M):
    name = sys.stdin.readline()
    # 개행제거
    name = name[:-1]

    if i < N:
        n.add(name)
    else:
        m.add(name)

l = sorted(n & m)

print(len(l))

for i in l:
    print(i)
