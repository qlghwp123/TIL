def factorial(N):
    if N == 0 or N == 1:
        return 1
    else:
        return N * factorial(N - 1)


N = int(input())

print(factorial(N))