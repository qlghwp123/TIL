M = int(input())

cup = [1, 0, 0]
for _ in range(M):
    first, second = map(lambda x: int(x) - 1, input().split())

    cup[first], cup[second] = cup[second], cup[first]

for i in range(len(cup)):
    if cup[i]:
        print(i + 1)