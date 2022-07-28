N = int(input())

result = {}
for _ in range(N):
    val = int(input())
    if val in result:
        result[val] += 1
    else:
        result[val] = 0

val = max(result.values())
# 람다 내 조건이 두 수를 볼 때 첫 번째 기준이 만약에 같으면
# 두 번째 기준으로 정렬하겠다는 의미이다.
result = sorted(result.items(), key=lambda x: (-x[1], x[0]))

print(result[0][0])