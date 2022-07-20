T = int(input())

for i in range(T):
    N = int(input())

    result = N * (N + 1) // 2
    even = (N // 2) * ( (N // 2) + 1 )

    print(f"#{i + 1}", result - even * 2)

