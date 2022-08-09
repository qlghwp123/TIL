# 못풀겠어서 참조함
# https://velog.io/@hygge/Python-%EB%B0%B1%EC%A4%80-2615-%EC%98%A4%EB%AA%A9-Brute-Force
# https://ywtechit.tistory.com/150

# 저렇게 1. while 문을 짜고 2. while 문 안에 조건을 설정하는 것
# 을 못해서 못풀었는데 좀 천천히 글을 쓰면서 했으면 나도 도출했을거
# 같은데 참 아쉽다.

dx = [-1, 0, 1, 1]
dy = [1, 1, 0, 1]

def check():
    board = []
    for _ in range(19):
        board.append(list(map(int, input().split())))

    for i in range(19):
        for j in range(19):
            if board[i][j] == 1 or board[i][j] == 2:
                cur = board[i][j]

                for k in range(4):
                    nx = i + dx[k]
                    ny = j + dy[k]
                    five = 1

                    while -1 < nx < 19 and -1 < ny < 19 and cur == board[nx][ny]:
                        five += 1
                        
                        # 오목일 때
                        if five == 5:
                            # 만약 다음 점이 같을 경우 육목
                            if -1 < nx + dx[k] < 19 and -1 < ny + dy[k]< 19 and board[nx][ny] == board[nx + dx[k]][ny + dy[k]]:
                                break
                            # 젤 처음 i, j 이전 값이 같을 경우 육목
                            if -1 < i - dx[k] < 19 and -1 < j - dy[k] < 19 and cur == board[i - dx[k]][j - dy[k]]:
                                break
                            return cur, (i + 1, j + 1)

                        nx += dx[k]
                        ny += dy[k]

    return 0, ()

win, coordi = check()
print(win)
if win:
    print(*coordi)

# 반례 모음
# https://www.acmicpc.net/board/view/83278
# 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 2
# 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 2 0
# 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 2 0 0
# 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 2 0 0 0
# 0 0 0 0 0 0 0 0 0 0 0 0 0 2 2 0 0 0 0
# 0 0 0 0 0 0 0 0 0 0 0 0 0 2 2 2 2 2 2
# 0 0 0 0 0 0 0 0 0 0 0 0 0 2 2 0 0 0 0
# 0 0 0 0 0 0 0 0 0 0 0 0 0 2 0 2 0 0 0
# 0 0 0 0 0 0 0 0 0 0 0 0 0 2 0 0 2 0 0
# 0 0 0 0 0 0 0 0 0 0 0 0 0 2 0 0 0 2 0
# 0 0 0 0 0 0 0 0 0 0 0 0 0 0 2 2 2 2 2