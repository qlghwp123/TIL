a_score = list(map(int, input().split()))
b_score = list(map(int, input().split()))

# 같으면 싹다 무승부로 둘 다 10점
if a_score == b_score:
    print("10 10", 'D', sep='\n')
else:
    total = [0, 0]
    result = []
    for i in range(10):
        if a_score[i] > b_score[i]:
            total[0] += 3
            result.append('A')
        elif a_score[i] < b_score[i]:
            total[1] += 3
            result.append('B')
        else:
            total[0] += 1
            total[1] += 1

    print(total[0], total[1])
    # A가 크면 A, B가 크면 B, 같으면 맨 마지막 결과난거 출력
    print('A' if total[0] > total[1] else ('B' if total[0] < total[1] else result[-1]))