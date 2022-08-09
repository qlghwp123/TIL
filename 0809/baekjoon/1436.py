N = int(input())

end = "666"
ret = []
i = 0
while(1):
    if end in str(i):
        ret.append(i)
    if len(ret) == N:
        break
    i += 1

print(ret[N - 1])


# 모든 경우에 통용되는 규칙을 못찾겠다.
# 아래는 내가 작성한 코드이다.

# end = "666"
# ret = []
# six = 0
# for i in range(N):
#     if i % 10 != 6:
#         ret.append(int(str(i) + end))
#     else:
#         ret += [int(str(i // 10) + end + str(j)) for j in range(10)]

# for i in enumerate(ret):
#     print(i)
