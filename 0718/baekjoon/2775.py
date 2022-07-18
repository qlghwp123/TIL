# T = int(input())

# # 0층
# apt = [[i for i in range(1, 15)]]

# # 제한 값이 어차피 0 ~ 14층, 1~14호로 되어있으므로 다 구한다.
# # i : 층수
# for i in range(1, 15):
#     temp = []
#     # j : 호수
#     for j in range(1, 15):
#         # result : 해당 호수에 거주하고 있는 사람 수
#         result = 0

#         # i - 1 층 1호 ~ j호수까지 사람들 총합 구하기
#         for k in range(j):
#             result += apt[i - 1][k]
        
#         temp.append(result)

#     apt.append(temp)

# for i in range(T):
#     k = int(input())
#     n = int(input())

#     print(apt[k][n-1])

# 위는 내가 생각하기에 내가 풀었지만 지양해야하는 방향인거 같다.
# 아래는 질문 검색에서 누가 작성한 코드이다.

T = int(input())

for i in range(T):
    k = int(input())
    n = int(input())

    people = [i for i in range(1, n+1)]
    
    # 첫 번째 0층을 초기화하고 해당 리스트를 지속적으로 재활용하는 형식이다.
    # people[y] = people[y - 1] + people[y] 순으로 계속 되고
    # 어차피 갱신하고자하는 부분은 전 인덱스 부분과 현 단계 부분을 더해서 갱신하면 되므로
    # 2차원 배열 형태를 가지는게 아닌 1차원 배열을 계속 활용하는 방식으로
    # 이렇게 간결하게 코드를 짠거 같다.

    for x in range(k):
        for y in range(1,n):
            people[y] += people[y-1]
    
    print(people[-1])