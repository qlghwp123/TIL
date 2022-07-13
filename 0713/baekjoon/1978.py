N = input()

l = list(map(int, input().split()))

result = len(l)

for i in l:
    count = 1
    while count <= i:
        if not i % count and 1 < count < i or i == 1:
            result -= 1
            break

        count += 1

print(result)