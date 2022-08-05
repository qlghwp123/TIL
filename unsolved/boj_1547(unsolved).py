M = int(input())

cup = [1, 2, 3]
for _ in range(M):
    first, second = map(lambda x: int(x) - 1, input().split())

    cup[first], cup[second] = cup[second], cup[first]

print(cup)
# for i in cup:
#     if i:
#         print(i + 1)