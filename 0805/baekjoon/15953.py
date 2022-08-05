T = int(input())

first_prize = [0, 5000000, 3000000, 2000000, 500000, 300000, 100000]
second_prize = [0] + [2 ** i * 10000 for i in range(9, 4, -1)]

temp = [0]
for i in range(1, len(first_prize)):
    temp += [first_prize[i]] * i

first_prize = temp

temp = [0]
for i in range(5):
    temp += [second_prize[i + 1]] * 2 ** i

second_prize = temp

for _ in range(T):
    first, second = map(int, input().split())

    ret = 0

    if first >= len(first_prize):
        first = 0
    if second >= len(second_prize):
        second = 0

    ret += first_prize[first]
    ret += second_prize[second]

    print(ret)