N = int(input())

# 1. 5로 나눔
# 2. 5로 나눈 몫을 저장
# 3. 3으로 나눔
# 4. 3으로 나눈 몫을 저장
# 5. 둘 다 몫이 0이면 -1 출력
# 6. 아니면 3으로 나눈 나머지를 구함
# 7. 3으로 나눈 나머지가 0이면 두 몫을 합해서 출력 아니면 -1 출력

# 위 방식은 못짜겠다. 따라서 다음과 같이
# 3, 6, 9, ... 처럼 나누기를 직접해서 차감한만큼의 값에 5로 나눴을 때,
# 나머지가 0 이면 3 * i, j 가 정답이 되는거고 아니면 계속 돈다.
# N = 18 의 경우 답이 2개가 있는데 처음 만난 것이 답이 되는 이유는
# 3이 5 보다 작으므로 3보다는 적은 수의 몫으로 5가 많은 수를 커버할 수 있다.
# 따라서 3과 5의 몫 조합이 두 번째 답보다 더 적은 수가 된다.
# 이 때, 범위는 3 * i 가 N 이하일 때까지 돈다.

result = -1

for i in range(0, N + 1, 3):
    R = (N - i) % 5
    j = (N - i) // 5

    if not R:
        result = i // 3 + j
        break

print(result)
