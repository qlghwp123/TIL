def sieve(N):
    # 1929.py 이용함.

    board = [True] * (N + 1)
    board[0] = board[1] = False

    i = 2
    while i * i <= N: 
        if board[i]:
            for j in range(i * i, N + 1, i):
                board[j] = False
        i += 1
    
    return board

n = 10000

T = int(input())

b = sieve(n)

for i in range(T):
    val = int(input())

    i = 2
    # 소수 조합이 여러 개인 경우 두 소수 쌍인 튜플을 저장하는 변수
    dupli = []
    # 소수 조합이 여러 개인 경우 두 소수 차이를 저장하는 변수
    # 초기값은 입력 값의 최댓값인 n 으로 설정했다.
    # 두 소수의 차이가 n의 최댓값을 넘을 수 없기 때문이다.
    abs_min = n
    while i < val:
        if b[i]:
            temp = val - i

            if b[temp]:
                # 두 소수 차이가 여러 개인 경우
                # 차이가 "작으면" 갱신한다.
                # 같거나 크면 갱신을 안한다.
                # 그래야 문제 결과처럼 8을 입력했을 때, 5, 3 이 아닌 3, 5 가 나온다. 
                if abs_min > abs(temp - i):
                    abs_min = abs(temp - i)
                    dupli.append((i, temp))
        i += 1
    
    print(dupli[-1][0], dupli[-1][1])
