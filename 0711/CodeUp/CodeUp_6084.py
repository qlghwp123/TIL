l = list(map(int, input().split()))

result = l[0] * l[1] * l[2] * l[3] / 8 / 1024 / 1024

print(f"{result:.1f} MB")