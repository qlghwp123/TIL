def factorial(N):
    # 0일 때를 처리 안하면 recursion error 가 뜬다.
    if N == 0 or N == 1:
        return 1
    else:
        return N * factorial(N - 1)


N = int(input())

print(factorial(N))