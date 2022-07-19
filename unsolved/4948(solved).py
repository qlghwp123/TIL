def sieve(N):
    # 1929.py 이용함.

    board = [True] * (N * 2 + 1)
    board[0] = board[1] = False

    i = 0
    while i * i <= N: 
        if board[i]:
            for j in range(i * i, N * 2 + 1, i):
                board[j] = False
        i += 1
    
    result = 0
    for i in range(N + 1, N * 2 + 1):
        if board[i]:
            result += 1

    return result

n = 1

while n != 0:
    n = int(input())

    if not n:
        break

    print(sieve(n))
