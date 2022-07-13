M = int(input())
N = int(input())

# M = 1 일 때 예외처리
if M == 1:
    M = 2

l = [ i for i in range(M, N+1)]
i = 2
result = list(filter(lambda x: x % i or x == i, l))

# https://ko.wikipedia.org/wiki/%EC%97%90%EB%9D%BC%ED%86%A0%EC%8A%A4%ED%85%8C%EB%84%A4%EC%8A%A4%EC%9D%98_%EC%B2%B4
while i * i <= N:
    i += 1
    result = list(filter(lambda x: x % i or x == i, result))

result = list(filter(lambda x: M <= x <= N, result))

# 둘 다 1일 때 예외처리
if M == 1 and N == 1:
    print(-1)
elif result:
    print(sum(result), result[0], sep='\n')
else:
    print(-1)