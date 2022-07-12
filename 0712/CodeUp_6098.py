b = [ list(map(int, input().split())) for i in range(10)]
done = 0

i, j = 1, 1
while i < 10:
    while j < 10:
        # 0인 경우 : 빈 공간
        if not b[i][j]:
            b[i][j] = 9
        # 1인 경우 : 벽
        elif b[i][j] == 1:
            # 왼쪽 아래가 벽이면 더 이상 갈 수 없다
            if b[i + 1][j - 1] == 1:
                done = 1
                break
            # 왼쪽 아래가 벽이 아니면 인덱스를 수정해준다.
            else:
                i += 1
                j -= 2
        # 2인 경우 : 먹이
        else:
            b[i][j] = 9
            done = 1
            break
        j += 1

    # 안쪽 반복문이 탈출하여 done 이라는 마킹 변수가 활성화되면 빠져 나온다.
    if done == 1:
        break

    i += 1

for i in range(10):
    for j in range(10):
        print(b[i][j], end=' ')
    print()