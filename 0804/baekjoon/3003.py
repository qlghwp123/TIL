rule = [1, 1, 2, 2, 2, 8]
found = list(map(int, input().split()))

for i in range(len(rule)):
    print(rule[i] - found[i], end=' ')