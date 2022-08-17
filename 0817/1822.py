na, nb = map(int, input().split())

a = set(map(int, input().split()))
b = set(map(int, input().split()))

if len(a - b):
    print(len(a - b))
    print(*(sorted(a - b)))
else:
    print(0)