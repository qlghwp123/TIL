T = int(input())

for i in range(T):
    result = sum(filter(lambda x: x % 2, map(int, input().split())))
    
    print(f"#{i + 1}", result)