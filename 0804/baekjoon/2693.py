T = int(input())

for _ in range(T):
    print(sorted(list(map(int, input().split())), reverse=True)[2])