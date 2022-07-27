T = int(input())

for i in range(T):
    l = input().split()
    # 한 글자 없애는 것을 슬라이싱을 활용했다.
    print(l[1][:int(l[0]) - 1] + l[1][int(l[0]):])