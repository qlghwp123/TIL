T = int(input())

for i in range(1, T + 1):
    val = list(map(int, input().split()))
    result = sum(val) / len(val)
    print(f"#{i}", round(result))