N = int(input())
forbid = [3, 6, 9]

for i in range(1, N + 1):
    result = list(filter(lambda x : x in forbid, map(int, list(str(i)))))

    if  result:
        print('-' * len(result), end=' ')
    else:
        print(i, end=' ')