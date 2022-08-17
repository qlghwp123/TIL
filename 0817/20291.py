import sys

input = sys.stdin.readline

T = int(input().rstrip())

d = {}

for _ in range(T):
    line = input().rstrip().split('.')

    if line[1] in d:
        d[line[1]] += 1
    else:
        d[line[1]] = 1

ret = sorted(d.items(), key=lambda x: x[0])

for k, v in ret:
    print(k, v)