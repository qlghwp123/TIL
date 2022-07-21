T = int(input())

for i in range(T):
    N = int(input())
    
    cp = N
    result = 1
    num = set()

    # 10이 됐을 때의 cp 값을 출력하는게 요구사항이다.
    # 문제를 너무 이상하게 서술해놨다.
    while len(num) != 10:
        num.update(list(str(cp)))
        if len(num) == 10:
            break
        result += 1
        cp = N * result

    print(f"#{i + 1}", cp)