T = int(input())

for i in range(1, T + 1):
    a, b = map(int, input().split())
    result = '>' if a > b else ('=' if a == b else '<')
    print(f"#{i}", result)