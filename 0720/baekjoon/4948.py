def sieve(N):
    # 1929.py 이용함.

    board = [True] * (N * 2 + 1)
    board[0] = board[1] = False

    i = 2
    # while 조건문에 N * 2 를 하는 것을 잊었다.
    while i * i <= N * 2: 
        if board[i]:
            for j in range(i * i, N * 2 + 1, i):
                board[j] = False
        i += 1
    
    result = 0
    # N + 1 이상 ~ N * 2 이하가 범위
    for i in range(N + 1, N * 2 + 1):
        if board[i]:
            result += 1

    return result

# 입력은 1 이상 ~ 123,456 이하이다.
n = 1

while n != 0:
    n = int(input())

    if not n:
        break

    print(sieve(n))
