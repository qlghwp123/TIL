N = int(input())
line = list(map(int, input().split()))

milk = [0, 1, 2]
count = 0
for i in line:
    if i == milk[count % 3]:
        count += 1

print(count)
