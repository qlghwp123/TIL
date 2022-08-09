R, C = map(int, input().split())

parking = []
for _ in range(R):
    parking.append(list(input()))

ret = dict.fromkeys([i for i in range(5)], 0)
for i in range(R - 1):
    for j in range(C - 1):
        temp = ""
        for k in range(2):
            for l in range(2):
                if -1 < i + k < R and -1 < j + k < C:
                    temp += parking[i + k][j + l]

        if '#' not in temp:
            for m in range(5):
                if m == temp.count('X'):
                    ret[m] += 1

for i in range(5):
    print(ret[i])