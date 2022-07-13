# 벌집은 1 부터 6, 12, 18, 24, ... 순으로 계속 해서 벌집의 개수가 "더해진다."
# N - 1 기준이며, 출발지, 도착지 제외할 경우 더해야할 리스트다.
# 1 : +1 default = 2 
# 2 ~ 6 : +0  default = 2
# 7 ~ 18 : +1 default = 2
# 19 ~ 36 : +2 default = 2
# 37 ~ 60 : +3 default = 2
# ...

N = int(input())

# 벌집의 개수를 찾는 hive 
# 6 * i 으로 점점 더 해야하므로 i는 현재 6의 배수를 의미한다.
hive = 0
i = 1
result = 1 if N == 1 else 0

while hive < N - 1:
    hive += 6 * i

    if hive >= N - 1:
        result = i - 1 + 2
    
    i += 1

print(result)