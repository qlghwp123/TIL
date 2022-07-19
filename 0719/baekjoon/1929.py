M, N = map(int, input().split())

# N + 2까지 커다란 보드를 만든다.
# 0, 1 은 안쓴다.
# (1, 2), (1, 3) 이라는 입력값이 들어오면 인덱스가 맞지 않는다.
# 따라서 2를 더 해준다.
board = [True] * (N + 2)
board[0] = board[1] = False

# https://ko.wikipedia.org/wiki/%EC%97%90%EB%9D%BC%ED%86%A0%EC%8A%A4%ED%85%8C%EB%84%A4%EC%8A%A4%EC%9D%98_%EC%B2%B4
i = 2

# N 보다 큰 제곱수는 볼 필요가 없다.
# 따라서 N 제곱근보다 작은 수만 보면 된다.
# (1, 2), (1, 3) 이라는 입력값이 들어와도
# 반복문이 돌지않지만 board 기본 값이 True 이기 때문에 걱정할 필요는 없다.
while i * i <= N: 
    # 에라토스체네스 규칙을 적용한 코드
    # 아래 링크를 보고 알았는데 바로 밑 if board[i]: 를 빼먹었다.
    # if 문을 달지 않으면 이미 False 처리된 인덱스에 대해서 연산을 계속해서 수행한다.
    # https://www.acmicpc.net/source/46271859
    if board[i]:
        for j in range(i * i, N + 1, i):
            board[j] = False
    i += 1

for i in range(M, N + 1):
    if board[i]:
        print(i)