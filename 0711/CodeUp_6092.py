n = int(input())
num = list(map(int, input().split()))

result = [0 for i in range(23)]
for i in num:
    result[i-1] += 1

for i in result:
    print(i, end=' ')