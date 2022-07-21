l = [0, 1]

def fibonacci(n):
    # 탈출 조건이면서 초기값일 경우.
    if n == 0 or n == 1:
        return l[n]
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

n = int(input())

print(fibonacci(n))
