l = list(map(int, input().split()))

result = l[0]
for i in range(1, l[3]):
    result = result * l[1] + l[2]

print(result)