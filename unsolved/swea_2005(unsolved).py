T = int(input())

for i in range(1, T + 1):
    N = int(input())

    triangle = [[] for _ in range(N)]

    print(f"#{i}")

    for j in range(N):
        for k in range(j + 1):
            if j < 2:
                triangle[j].append(1)
            else:
                if -1 < j - 1 < N:
                    if -1 < k - 1 < j:
                        triangle[j].append(triangle[j - 1][k - 1] + triangle[j - 1][k])
                else:
                    triangle[j].append(1)
        print()
    
    for j in triangle:
        print(*j)