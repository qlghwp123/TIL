n = int(input())
num = list(map(int, input().split()))

result = num[::-1]
for i in result:
    print(i, end=' ')