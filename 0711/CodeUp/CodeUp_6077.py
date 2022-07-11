N = int(input())

result = sum([i for i in range(1, N+1) if not i % 2])

print(result)
