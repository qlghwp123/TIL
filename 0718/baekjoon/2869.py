import math

A, B, V = map(int, input().split())

# 아래는 처음 작성한 코드.
# 하지만 시간이 너무 오래 걸리고 애초 문제에서 제시한 시간 제한을 아득히 초과한다.

# result = 0
# i = 0
# while result < V:
#     i += 1
#     result += A

#     if result >= V:
#         break
#     else:
#         result -= B

# print(i)

# 공책에 쓰면서 천천히 풀어보니 다음과 같다.
# 내가 뽑은 테스트 케이스
# T  A      B       V
# 1  2      1       5
# 2  5      1       6
# 3  100    99      1000000000
# 4  2      1       2
# 5  10     1       21
# 6  10     2       30

# 일단 위 테스트 케이스들을 손으로 써봤고 얼마만큼이 더해지는지도 적었다.

# T1
# i  A      A-B
# 1  2      1
# 2  3      2
# 3  4      3
# 4  5

# T2
# i  A      A-B
# 1  5      4
# 2  9

# T3
# i         A           A-B
# 1         100         1
# 2         101         2
# 3         102         3
#         ...
# 999999900 999999900   999999801
# 999999901 1000000000

# T4
# i  A A-B
# 1  2 

# T5
# i  A      A-B
# 1  10     9
# 2  19     18
# 3  28

# T6
# i  A      A-B
# 1  10     8
# 2  18     16
# 3  28     24
# 4  34

# 즉 A 가 A 값을 초항으로, A-B 를 공차로 등차수열을 이룸을 보았고
# A 의 등차수열 An 이 An >= V 를 만족하는 An 의 최솟값을 찾아서 n을 찾으면 그게 답이 된다.
# 이것을 내 식대로 써봤다.
# An >= V 를 찾으려고 한다.
# An = A + (n - 1) * d, d = (A - B) 이다. 
# An = A + (n - 1) * (A - B) 가 되고 이를 An >= V 를 대입하면
# A + (n - 1) * (A - B) >= V 가 된다.

# 식을 좀 풀어서 정리하면
# A + (A - B) * n - (A - B) >= V 므로 
# A + (A - B) * n - A + B >= V 
# (A - B) * n + B >= V 가 된다.

# 우리가 구하고자 하는 것은 n 이고 A, B, V 모두 문제에서 입력으로 제공하는 상수 값이다.
# 따라서 n 을 좌항에 혼자 남겨놓고 나머지는 우항으로 넘긴다.
# 정리하면 n >= (V - B) / (A - B) 가 된다.
# 이 때 최솟값이 되는건 곧 n == (V - B) / (A - B) 을 의미하므로
# (V - B) / (A - B) 값만 찾으면 끝이 난다.

# 단, 내가 생각을 잘못한건 n 은 자연수의 범위인데 
# (V - B) / (A - B) 가 자연수면 좋지만 실수가 나올 수 있음을 잊었다.
# 즉 (V - B) / (A - B) 가 자연수 범위에서 만족하지 않을 수 있음을 망각했다.
# 따라서 (V - B) / (A - B) 가 실수가 나오면 천장함수의 인자로 사용 해야한다.
# 그래서 math.ceil() 메소드를 활용한 것이다.

# V == A 의 경우 바로 정상에 올라갔고
# 문제에서 "정상에 올라간 후에 미끄러지지 않는다" 라고 명시되어 있기 때문에
# 1만 출력해주면 끝이다.

if V == A:
    result = 1
else:
    result = math.ceil((V - B) / (A - B))

print(result)