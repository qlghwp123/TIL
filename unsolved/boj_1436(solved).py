N = int(input())

end = "666"
ret = []
# six = 0
# for i in range(N):
#     if i % 10 != 6:
#         ret.append(int(str(i) + end))
#     else:
#         ret += [int(str(i // 10) + end + str(j)) for j in range(10)]

# for i in enumerate(ret):
#     print(i)

i = 0
while(1):
    if end in str(i):
        ret.append(i)
    if len(ret) == N:
        break
    i += 1

for i in enumerate(ret):
    print(i)