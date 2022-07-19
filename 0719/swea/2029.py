T = int(input())

# 원래 입력 값 대소비교를 해야하지만 문제를 보니 항상 a > b 를 만족하는 값이 들어오는거 같다.

for i in range(T):
    a, b = map(int, input().split())
    print(f"#{i + 1}", a // b, a % b)