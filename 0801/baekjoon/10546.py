# import sys

# input = sys.stdin.readline

# N = int(input())

# attendance = {}
# for _ in range(N):
#     runner = input()

#     # 두 번째는 동명이인 존재 수
#     if runner not in attendance:
#         attendance[runner] = [1, 0]
#     else:
#         attendance[runner][1] += 1

# for _ in range(N - 1):
#     runner = input()

#     if runner in attendance:
#         if attendance[runner][1] > 0:
#             attendance[runner][1] -= 1
#         else:
#             del attendance[runner]

# print(list(attendance.keys())[0].strip())

# 아래는 다른 사람 코드
# https://www.acmicpc.net/source/46998407
# 생각 해보니 삭제시켜도 됐다. 어차피 하나 빼고 모조리 없애면 되니까...

# import sys
# input = sys.stdin.readline
# T = int(input())
# result = {}
# for i in range(T*2 - 1):
#     names = input()
#     if names not in result:
#         result[names] = 1
#     else:
#         del result[names]
# print(*result)