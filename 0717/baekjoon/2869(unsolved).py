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