T = int(input())

for i in range(T):
    line = list(map(int, input().split()))

    # 문제 공식 그대로 사용
    result = (sum(map(lambda x: x*2, line[::2])) + sum(line[1::2])) % 10
    # 10에서 부족한 것이기에, 더하는 수를 구하는 것이므로 빼야함.
    result = result if not result else (10 - result)

    print(f"#{i + 1}", result)