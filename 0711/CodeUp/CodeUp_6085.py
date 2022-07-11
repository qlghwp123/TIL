l = list(map(int, input().split()))

result = l[0] * l[1] * l[2] / 8 / 1024 / 1024

print(f"{result:.2f} MB")