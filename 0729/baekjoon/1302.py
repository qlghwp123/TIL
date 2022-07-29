import sys

N = int(input())

d = {}
for _ in range(N):
    # readline 은 개행을 포함시킨다.
    val = sys.stdin.readline()
    val = val[:-1]

    if val not in d:
        d[val] = 1
    else:
        d[val] += 1

l = sorted(d.items(), key=lambda x: (-x[1], x[0]))

print(l[0][0])