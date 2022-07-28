import sys

N = int(input())

# 입력 값 받기
result = []
for _ in range(N):
    # 여러 줄을 입력 값으로 받을 때, sys.stdin.readline() 을 써야한다고 한다.
    # 실제로 써보니 시간 초과가 나지 않았다.
    # result.append(int(input()))
    result.append(int(sys.stdin.readline()))

# 산술평균을 위한 정렬된 입력값 복사본
cp = sorted(result)

# 각 값에 대한 빈도를 구하기
temp = {}
for i in cp:
    if i not in temp:
        temp[i] = 1
    else:
        temp[i] += 1

# 빈도 수를 기준으로 정렬
dict_list = sorted(temp.items(), key=lambda x: (-x[1], x[0]))
val_list = list(temp.values())

# 최대 빈도 수가 중복이 있는지 검사
cnt = val_list.count(dict_list[0][1])
if cnt > 1:
    val = dict_list[1][0]
else:
    val = dict_list[0][0]

# 출력값 계산
arithmetic_mean = round(sum(result) / N)
median = cp[N//2]
mode = val
scope = cp[-1] - cp[0]

print(arithmetic_mean, median, mode, scope, sep='\n')
