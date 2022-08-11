T = int(input())

prime = [2, 3, 5, 7, 11]

for i in range(1, T + 1):
    N = int(input())

    l = []

    for j in prime:
        count = 0
        temp = N

        while True:
            count += 1

            if not temp % j:
                temp //= j
            else:
                count -= 1
                break
            
        l.append(count)

    print(f"#{i}", *l)