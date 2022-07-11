N = int(input())
l = [3, 6 , 9]

for i in range(1, N+1):
    if i % 10 in l or i // 1 in l:
        print("X", end=" ")
    else:
        print(i, end=" ")