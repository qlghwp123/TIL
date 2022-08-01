# https://calcproject.tistory.com/559
# https://www.acmicpc.net/board/view/91772
# https://www.acmicpc.net/board/view/93452
# https://www.acmicpc.net/board/view/95312
import sys

T = int(input())

# 나누어 떨어지는 경우를 맨 앞으로 뒀다.
# 원래 순서는 맨 앞 요소가 맨 뒤로 온다.
first = {
    0: [10],
    1: [1],
    2: [6, 2, 4, 8],
    3: [1, 3, 9, 7],
    4: [6, 4],
    5: [5],
    6: [6],
    7: [1, 7, 9, 3],
    8: [6, 8, 4, 2],
    9: [1, 9]
}

for _ in range(T):
    a, b = map(int, sys.stdin.readline().split())

    first_idx = a % 10
    second_idx = b % len(first[first_idx])

    print(first[first_idx][second_idx])